from jinja2 import Environment, PackageLoader, select_autoescape
import mdformat
from yaml import load, Loader


def main():
    # Get contract parameters
    with open("contract_params.yml", "r") as config_file:
        config = load(config_file, Loader=Loader)

    # print(config)

    # Look for the "template parameter" and attempt to load that template
    template_name = f'{config["template"]}.md.j2'
    # template_file = open(template_name, "r")

    env = Environment(
        loader=PackageLoader("generate_contract"),
        autoescape=select_autoescape()
    )
    template = env.get_template(template_name)

    rendered_document = template.render(config)

    # Jinja may generate very long lines or extraneous line breaks between paragraphs,
    # so we use mdformat to wrap long lines and remove sequences of more than two
    # consecutive line breaks. Note that mdformat does not wrap text by default.
    # Wraps lines to 88 characters, like Black does.
    # https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length
    formatted_document = mdformat.text(
        rendered_document,
        options={
            "wrap": 88,
        },
    )

    print(formatted_document)


if __name__ == "__main__":
    main()
