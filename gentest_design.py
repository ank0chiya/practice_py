class Table:
    def __init__(self, dirname, suffix):
        self.suffix = suffix
        self.filename = ""
        self.formated_tbl = self.fotmat_tbl(dirname, suffix)
        self.base_data = {}

    def read_file(self):
        pass

    def format_tbl(self, base_data, suffix):
        self.formated_tbl = TblFormatter(suffix)


class TblFormatter:
    def __init__(self, base_data, suffix) -> None:
        self.suffix = suffix
        self.format_tbl = self.format_tbl(base_data)

    def format_tbl(self, base_data):
        if self.suffix == ("param" or "cond"):
            self.format_tbl = ParamFormatter(base_data)
        elif self.suffix == ("smt" or "chk"):
            self.format_tbl = ActionFormatter(base_data)
        elif self.suffix == ("page" or "pagecond"):
            self.format_tbl = PageFormatter(base_data)
        else:
            raise NotImplementedError

class ParamFormatter(TblFormatter):
    def format_tbl(self, base_data):
        print("PARAM Formatter", base_data)

class ActionFormatter(TblFormatter):
    def format_tbl(self, base_data):
        print("ACTION Formatter", base_data)

class PageFormatter(TblFormatter):
    def format_tbl(self, base_data):
        print("PAGE Formatter", base_data)




         



         