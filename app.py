import os
import click
from core.collector import adpu_q_get_all_links
from core.constants import header, ARTICLES_DIR

@click.command()
@click.option("--step", prompt="Step", help="collect -> Collect Articles      merge -> Merge Articles") 
@click.option("--url", default="https://adpuquba.edu.az/ilham-heyd%c9%99r-oglu-%c9%99liyevin-ilk-d%c9%99f%c9%99-prezident-secilm%c9%99sind%c9%99n-18-il-otur/", prompt="Url", help="Url unvanini daxil edin") 
def main(step, url):
    if step == "collect":
        adpu_q_get_all_links(url=url, header=header, limit=1)
    elif step == "merge":
        text = ''
        with open(os.getcwd()+ARTICLES_DIR+"merged.txt", "w") as merged_f:
            for file in os.listdir(os.getcwd()+ARTICLES_DIR):
                with open(os.getcwd()+ARTICLES_DIR+file, "r") as _f:
                    text = _f.read()
                merged_f.write(text)
    else:
        return False


if __name__ == '__main__':
    main()

        
