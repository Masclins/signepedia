diccionari_correcte <- function(diccionari) {
  nota_correcte <- !grepl("embed", diccionari$nota)
  origen_correcte <- (diccionari$origen == "youtube") | (diccionari$origen == "")
  autor_correcte <- (diccionari$autor != "")
  correcte <- nota_correcte & origen_correcte & autor_correcte
  
  if (sum(correcte) == nrow(diccionari)) {
    return(TRUE)
  } else {
    print("Hi ha paraules amb camps erronis: ")
    print(diccionari[!correcte, "paraula"])
    return(FALSE)
  }
}

ordenar_alfabeticament <- function() {
  ruta_diccionari = "../backend/diccionari.csv"
  tryCatch({
    data <- read.csv(ruta_diccionari, fileEncoding="utf-8", stringsAsFactors = FALSE)
    
  }, warning = function(w) {
    print(w)
  }, error = function(e) {
    print(e)
  }, finally = {

    if (diccionari_correcte(data)) {
      data <- data[order(data[,"nota"]),]
      data <- data[order(data[,"paraula"]),]
      write.csv(data, ruta_diccionari, fileEncoding="utf-8", row.names=FALSE)
    }
  })
}

actualitzar_pendents <- function() {
  ruta_diccionari = "../backend/diccionari.csv"
  ruta_pendents = "../paraules_pendents.txt"
  diccionari <- read.csv(ruta_diccionari, fileEncoding="utf-8", stringsAsFactors = FALSE)
  pendents <- read.table(ruta_pendents, fileEncoding="utf-8", stringsAsFactors = FALSE)[,1]
  
  if (diccionari_correcte(diccionari)) {
    expresions <- sapply(apply(diccionari[,1:2], 1, paste, collapse = " "), trimws)
  
    pendents <- data.frame(pendents[!sapply(pendents, function(p){p %in% expresions})])

    write.table(pendents, ruta_pendents, fileEncoding="utf-8", row.names=FALSE, col.names=FALSE)
  }
}

paraules_repetides <- function() {
  ruta_diccionari = "../backend/diccionari.csv"
  diccionari <- read.csv(ruta_diccionari, fileEncoding="utf-8", stringsAsFactors = FALSE)
  
  expresions <- sapply(apply(diccionari[,1:2], 1, paste, collapse = " "), trimws)
  diccionari[duplicated(expresions),1:2]
}

videos_sense_us <- function() {
  ruta_diccionari = "../backend/diccionari.csv"
  diccionari <- read.csv(ruta_diccionari, fileEncoding="utf-8", stringsAsFactors = FALSE)
  urls <- diccionari[,"url"]
  videos <- paste0("videos/", list.files("../frontend/public/videos/"))
  
  videos[!sapply(videos, function(v){v %in% urls})]
}
