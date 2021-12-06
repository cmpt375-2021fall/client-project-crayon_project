import pdfkit

 
def html_to_string(html, to_file):
    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_string(html, to_file, configuration=config)
    print('完成')

 