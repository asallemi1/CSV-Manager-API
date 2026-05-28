import pandas as pd

class CsvManager:

    def __init__(self, csv_file):
        self.set_csv(csv_file)

    def set_csv(self, csv_file):
        if csv_file is None or not csv_file.endswith(".csv"):
            raise ValueError("Inserire un file csv")
        self.__csv_file = csv_file

    def get_csv_file(self):
        return self.__csv_file

    def write_csv(self, df):
        df.to_csv(self.__csv_file, index=False)

    def rows_csv(self, mode, n_rows=5):
        df = pd.read_csv(self.__csv_file)

        if mode == "head":
            return df.head(n_rows)
        elif mode == "tail":
            return df.tail(n_rows)
        else:
            raise ValueError("Inserire head or tail")

    def info_csv(self):
        df = pd.read_csv(self.__csv_file)
        return {
            "columns": list(df.columns),
            "dtypes": df.dtypes.astype(str).to_dict()
        }

    def describe_csv(self):
        return pd.read_csv(self.__csv_file).describe()

    def shape_csv(self):
        return pd.read_csv(self.__csv_file).shape

    def columns_csv(self):
        return list(pd.read_csv(self.__csv_file).columns)

    def pivot_csv(self, values, index, aggfunc):
        return pd.read_csv(self.__csv_file).pivot_table(values, index, aggfunc=aggfunc)
