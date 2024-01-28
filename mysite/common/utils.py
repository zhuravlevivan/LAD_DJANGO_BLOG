from datetime import datetime as dt
from django.template.defaultfilters import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


def get_image_path(instance, filename):
    """Обработка кириллицы в имени загружаемой картинки"""
    now = dt.now()
    name, ext = filename.rsplit('.', 1)

    # return os.path.join(instance._meta.model_name.lower(),
    #                     now.strftime("%Y"),
    #                     now.strftime("%m"),
    #                     now.strftime("%d"),
    #                     f'{slugify(name)}.{ext}')
    return '/'.join((instance._meta.model_name.lower(), now.strftime('%Y/%m/%d'), f'{slugify(name)}.{ext}'))
