import function


def main(myfile):
   function.loggerMain.info("...Leyendo el archivo...")
   try:
        with open(myfile, "r") as f:
            file = f.readlines()
            function.loggerMain.info("...Archivo procesado...")
            info_extract = function.info_lines(myfile)
            word_count = function.word_counter(info_extract[1])
   except Exception:
      function.loggerMain.error("No se pudo abrir el archivo",
                                exc_info=True)
   return myfile

if __name__ == '__main__':
   main('C:\\Users\\cris\\Desktop\\PrismaRun-Alkemy\\Loguear-Eventos-2-Practica-4\\editorial\\cuento.txt')