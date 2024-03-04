# This file generated by Quarto; do not edit by hand.

from __future__ import annotations

from pathlib import Path
from shiny import App, Inputs, Outputs, Session, ui

import seaborn as sns
from shiny import render, reactive, ui
penguins = sns.load_dataset("penguins")

ojs_define(pythondata = penguins)

# ========================================================================




def server(input: Inputs, output: Outputs, session: Session) -> None:


    return None


_static_assets = ["Shiny Python and Observable_files"]
_static_assets = {"/" + sa: Path(__file__).parent / sa for sa in _static_assets}

app = App(
    Path(__file__).parent / "Shiny Python and Observable.html",
    server,
    static_assets=_static_assets,
)
