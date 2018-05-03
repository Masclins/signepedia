ordenar_alfabeticament <- function(ruta = "../backend/diccionari.csv") {
  data <- read.csv(ruta, fileEncoding="utf-8")
  data <- data[order(data[,"paraula"]),]
  write.csv(data, ruta, fileEncoding="utf-8", row.names=FALSE)
}

actualitzar_pendents <- function(ruta_diccionari = "../backend/diccionari.csv", ruta_pendents = "../paraules_pendents.txt") {
  diccionari <- read.csv(ruta_diccionari, fileEncoding="utf-8", stringsAsFactors = FALSE)
  pendents <- read.table(ruta_pendents, fileEncoding="utf-8", stringsAsFactors = FALSE)
  
  pendents <- data.frame(pendents[!sapply(pendents, function(p){p %in% diccionari$paraula})])
  
  write.table(pendents, ruta_pendents, fileEncoding="utf-8",row.names=FALSE,col.names=FALSE)
}
