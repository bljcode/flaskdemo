from flask import render_template, session, redirect, url_for
from . import main
from ..models import example


@main.route('/strategy', methods=['GET', 'POST'])
def strategy():
    re = example.importtest("fan")
    return 'in strategy!' + re


if __name__ == '__main__':
    pass
