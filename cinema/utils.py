# flake8: noqa: E501

import pathlib
import uuid
from typing import TYPE_CHECKING

from django.utils.text import slugify

if TYPE_CHECKING:
    from .models import Movie


def get_image_path(instance: "Movie", filename: str) -> pathlib.Path:
    filename = f"{slugify(instance.title)}-{uuid.uuid4}" + pathlib.Path(filename).suffix
    return pathlib.Path("upload/movies/") / pathlib.Path(filename)
