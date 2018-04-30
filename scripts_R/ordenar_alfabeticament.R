ordenar_alfabeticament <- function(ruta = "../backend/diccionari.csv") {
  data <- read.csv(ruta, fileEncoding="utf-8")
  data <- data[order(data[,"paraula"]),]
  write.csv(data, ruta, fileEncoding="utf-8", row.names=FALSE)
}
