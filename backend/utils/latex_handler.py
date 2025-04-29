import subprocess

def read_latex_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def write_latex_file(content: str, filename: str) -> str:
    path = f"./cvs/{filename}.tex"
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
        print(content)
    return path

def compile_latex_to_pdf(tex_path: str, output_dir: str = "./cvs") -> str:
    try:
        subprocess.run(
            ["pdflatex", "-output-directory", output_dir, tex_path],
            check=True
        )
        pdf_filename = tex_path.replace(".tex", ".pdf")
        return pdf_filename
    except FileNotFoundError as e:
        print("pdflatex not found! Check path.")
        raise
    except subprocess.CalledProcessError as e:
        print("Error compiling LaTeX:", e)
        return ""
