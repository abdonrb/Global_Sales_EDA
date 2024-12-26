import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class AutoPlot:
    """
    Clase para crear gráficos automáticamente en función de las variables y sus tipos.
    """
    def __init__(self, data):
        """
        Inicializa la clase con un DataFrame.

        :param data: DataFrame de pandas que contiene los datos.
        """
        self.data = data

    def univariate_plot(self, variables, types):
        """
        Genera gráficos univariantes para las variables especificadas.

        :param variables: Lista de nombres de columnas a graficar.
        :param types: Lista de tipos correspondientes a cada columna (nominal, ordinal, continuo, discreto, fecha).
        """
        for var, var_type in zip(variables, types):
            plt.figure(figsize=(8, 6))
            
            if var_type in ["nominal", "ordinal"]:
                sns.countplot(y=self.data[var], palette="viridis")
                plt.title(f"Frecuencia de {var}")

            elif var_type in ["continuo", "discreto"]:
                sns.histplot(self.data[var], kde=True, bins=30, color="blue")
                plt.title(f"Distribución de {var}")

            elif var_type == "fecha":
                self.data[var] = pd.to_datetime(self.data[var])
                self.data[var].value_counts().sort_index().plot()
                plt.title(f"Serie temporal de {var}")

            plt.xlabel(var)
            plt.ylabel("Frecuencia")
            plt.tight_layout()
            plt.show()

    def bivariate_plot(self, variables, types):
        """
        Genera gráficos bivariantes para pares de variables especificadas.

        :param variables: Lista de nombres de columnas (dos columnas).
        :param types: Lista de tipos correspondientes a cada columna (nominal, ordinal, continuo, discreto, fecha).
        """
        if len(variables) != 2:
            raise ValueError("Se requieren exactamente dos variables para gráficos bivariantes.")

        var_x, var_y = variables
        type_x, type_y = types

        plt.figure(figsize=(10, 6))

        if type_x in ["nominal", "ordinal"] and type_y in ["nominal", "ordinal"]:
            sns.countplot(x=self.data[var_x], hue=self.data[var_y], palette="viridis")
            plt.title(f"Distribución de {var_x} por {var_y}")

        elif type_x in ["continuo", "discreto"] and type_y in ["continuo", "discreto"]:
            sns.scatterplot(x=self.data[var_x], y=self.data[var_y], color="blue")
            plt.title(f"Relación entre {var_x} y {var_y}")

        elif type_x in ["nominal", "ordinal"] and type_y in ["continuo", "discreto"]:
            sns.boxplot(x=self.data[var_x], y=self.data[var_y], palette="viridis")
            plt.title(f"Distribución de {var_y} por {var_x}")

        elif type_x == "fecha" or type_y == "fecha":
            self.data[var_x] = pd.to_datetime(self.data[var_x])
            sns.lineplot(x=self.data[var_x], y=self.data[var_y])
            plt.title(f"Tendencia de {var_y} a lo largo de {var_x}")

        plt.tight_layout()
        plt.show()

    def multivariate_plot(self, variables, types):
        """
        Genera gráficos multivariantes para un c<onjunto de variables especificadas.

        :param variables: Lista de nombres de columnas.
        :param types: Lista de tipos correspondientes a cada columna (nominal, ordinal, continuo, discreto, fecha).
        """
        numeric_vars = [var for var, var_type in zip(variables, types) if var_type in ["continuo", "discreto"]]

        if len(numeric_vars) >= 2:
            sns.pairplot(self.data[numeric_vars], diag_kind="kde", palette="viridis")
            plt.suptitle("Gráficos de pares para variables numéricas", y=1.02)
            plt.show()

        else:
            raise ValueError("Se requieren al menos dos variables numéricas para gráficos multivariantes.")
        
# Ejemplo de uso
# data = pd.read_csv("tu_dataset.csv")
# plotter = AutoPlot(data)
# plotter.univariate_plot(["edad", "genero"], ["continuo", "nominal"])
# plotter.bivariate_plot(["edad", "ingresos"], ["continuo", "continuo"])
# plotter.multivariate_plot(["edad", "ingresos", "gastos"], ["continuo", "continuo", "continuo"])