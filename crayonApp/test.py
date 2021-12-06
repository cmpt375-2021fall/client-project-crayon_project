import pdfkit
import platform
import os,sys, subprocess, platform
 
def html_to_string(html, to_file):
    if platform.system() == 'Windows':
        pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
    else:
       os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable) 
       WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], 
            stdout=subprocess.PIPE).communicate()[0].strip()
       pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
 
    pdfkit.from_string(html, to_file, configuration=pdfkit_config)


 