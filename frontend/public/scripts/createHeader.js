function writeHeader(JSONstr) {
    if (JSONstr === "") {

document.write(
    "<header>" +
      "<div>" +
        "<a href=\"/\"><img src=\"/images/logo.png\" alt=\"Signepèdia\" height=\"120\" width=\"auto\"></a>" +
      "</div>" +
      "<div>" +
        "<form action=\"/register\", method=\"get\">" +
          "<button type=\"submit\" class=\"icon-button\">" +
            "<i class=\"fa fa-sign-in\">&nbsp;Registra't</i>" +
          "</button>" +
        "</form>" +
      "</div>" +
    "</header>");

    }
}
