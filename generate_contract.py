from jinja2 import Environment, PackageLoader, select_autoescape
from yaml import load, Loader


def main():
    # Get contract parameters
    with open("contract_params.yml", "r") as config_file:
        config = load(config_file, Loader=Loader)

    print(config)

    # Look for the "template parameter" and attempt to load that template
    template_name = f'{config["template"]}.md.j2'
    # template_file = open(template_name, "r")

    env = Environment(
        loader=PackageLoader("generate_contract"),
        autoescape=select_autoescape()
    )
    template = env.get_template(template_name)

    rendered_document = template.render(config)
    print(rendered_document)


if __name__ == "__main__":
    main()
