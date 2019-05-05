import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def get_all_file_name(dir):
    """
    This function get all pdf file in the same dir and return sorted list.
    :param dir: ready to merge pdf file's dir path.
    :return: files name list sorted by create time.
    """
    file_list = os.listdir(dir)
    file_list = [os.path.join(dir, x) for x in sorted(file_list,  key=lambda x: os.path.getctime(os.path.join(dir, x)))]
    return file_list if file_list else []


def merge_pdf(filepath, outfile):
    """
    This function means to merge all pdf in same dir and generate a new pdf file.
    :param filepath: pdf files path.
    :param outfile: generated new pdf file's name like: text.pdf
    :return:
    """
    output = PdfFileWriter()
    output_pages = 0
    pdf_files_names = get_all_file_name(filepath)

    if pdf_files_names:
        for pdf_file in pdf_files_names:
            print("[Open]:%s" % pdf_file)
            input = PdfFileReader(open(pdf_file, "rb"))

            page_count = input.getNumPages()
            output_pages += page_count
            for page in range(page_count):
                output.addPage(input.getPage(page))
        print("[Page]: %d" % output_pages)

        with open(os.path.join(filepath, outfile), "wb") as output_stream:
            output.write(output_stream)
        print("[Merge]: Over.")
    else:
        print("[Warning]: No PDF file ready to merge.")
