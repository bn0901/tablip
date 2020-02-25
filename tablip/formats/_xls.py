""" Tablib - XLS Support.
"""

from io import BytesIO

import tablip
import xlrd
import xlwt

# special styles
wrap = xlwt.easyxf("alignment: wrap on")
bold = xlwt.easyxf("font: bold on")


class XLSFormat:
    title = 'xls'
    extensions = ('xls',)

    @classmethod
    def detect(cls, stream):
        """Returns True if given stream is a readable excel file."""
        try:
            xlrd.open_workbook(file_contents=stream)
            return True
        except Exception:
            pass
        try:
            xlrd.open_workbook(file_contents=stream.read())
            return True
        except Exception:
            pass
        try:
            xlrd.open_workbook(filename=stream)
            return True
        except Exception:
            return False

    @classmethod
    def export_set(cls, dataset):
        """Returns XLS representation of Dataset."""

        wb = xlwt.Workbook(encoding='utf8') # 用xlwt建立工作簿-一个文件
        ws = wb.add_sheet(dataset.title if dataset.title else 'Tablib Dataset') # 对工作簿对象加一张表，表头名字为这个dataset的头

        cls.dset_sheet(dataset, ws) # 往表中加dataset数据

        stream = BytesIO()
        wb.save(stream)
        return stream.getvalue()

    @classmethod
    def export_book(cls, databook):
        """Returns XLS representation of DataBook."""

        wb = xlwt.Workbook(encoding='utf8')

        for i, dset in enumerate(databook._datasets):
            ws = wb.add_sheet(dset.title if dset.title else 'Sheet%s' % (i))

            cls.dset_sheet(dset, ws)

        stream = BytesIO()
        wb.save(stream)
        return stream.getvalue()

    @classmethod
    def import_set(cls, dset, in_stream, headers=True):
        """Returns databook from XLS stream."""

        dset.wipe()

        xls_book = xlrd.open_workbook(file_contents=in_stream.read())
        sheet = xls_book.sheet_by_index(0)

        dset.title = sheet.name

        for i in range(sheet.nrows):
            if i == 0 and headers:
                dset.headers = sheet.row_values(0)
            else:
                dset.append([
                    val if typ != xlrd.XL_CELL_ERROR else xlrd.error_text_from_code[val]
                    for val, typ in zip(sheet.row_values(i), sheet.row_types(i))
                ])

    @classmethod
    def import_book(cls, dbook, in_stream, headers=True):
        """Returns databook from XLS stream."""

        dbook.wipe()

        xls_book = xlrd.open_workbook(file_contents=in_stream)

        for sheet in xls_book.sheets():
            data = tablip.Dataset()
            data.title = sheet.name

            for i in range(sheet.nrows):
                if i == 0 and headers:
                    data.headers = sheet.row_values(0)
                else:
                    data.append(sheet.row_values(i))

            dbook.add_sheet(data)

    @classmethod
    def get_col_width(cls,data):
        row_length = 100 if len(data)>100 else len(data)
        col_length = 20 if len(data[0])>20 else len(data[0])
        col_width = {}
        for n in range(col_length):
            a = 0
            for m in range(row_length):
                content = data[m][n]
                if content != None and content!='' and len(str(content))>a:   #第m行的第n列的字数 如果比a大，则保存a为最大数
                    a = len(str(content))
            col_width[n] = a

        return col_width


    @classmethod
    def dset_sheet(cls, dataset, ws):
        """Completes given worksheet from given Dataset."""
        _package = dataset._package(dicts=False)  # 转化全部数据表数据为一个list，每个项为每一行。
        col_width = cls.get_col_width(_package)

        for i, sep in enumerate(dataset._separators):
            _offset = i
            _package.insert((sep[0] + _offset), (sep[1],))

        for i, row in enumerate(_package):
            for j, col in enumerate(row):

                # bold headers 如果第一行，且dataset是有表头的。则写表头
                if (i == 0) and dataset.headers:
                    ws.col(j).width = (col_width[j]+3) * 256  # 设置某列宽度为256*字数,由于还是会短一点点，所以再加3个字符使显示全
                    ws.write(i, j, col, bold) # 第几行|第几列|内容|style

                    # frozen header row
                    ws.panes_frozen = True
                    ws.horz_split_pos = 1

                # bold separators
                elif len(row) < dataset.width:
                    ws.write(i, j, col, bold)

                # wrap the rest
                else:
                    try:
                        if '\n' in col:
                            ws.write(i, j, col, wrap)
                        else:

                            ws.write(i, j, col)
                    except TypeError:
                        ws.write(i, j, col)
