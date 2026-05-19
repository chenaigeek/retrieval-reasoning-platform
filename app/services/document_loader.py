from pypdf import PdfReader


def load_pdf(file):

    reader = PdfReader(file)

    text = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


def load_text(content):

    return content.decode("utf-8")
