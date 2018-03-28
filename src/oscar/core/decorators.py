try:
    from types import ClassType
except ImportError:
    # Python 3
    CHECK_TYPES = (type,)
else:
    # Python 2: new and old-style classes
    CHECK_TYPES = (type, ClassType)
import warnings

from oscar.utils.deprecation import RemovedInOscar20Warning


def deprecated(obj):
    if isinstance(obj, CHECK_TYPES):
        return _deprecated_cls(cls=obj)
    else:
        return _deprecated_func(f=obj)


def _deprecated_func(f, warn_cls=RemovedInOscar20Warning):
    def _deprecated(*args, **kwargs):
        message = "Method '%s' is deprecated and will be " \
            "removed in the next version of JUS" \
            % f.__name__
        warnings.warn(message, warn_cls, stacklevel=2)
        return f(*args, **kwargs)
    return _deprecated


def _deprecated_cls(cls, warn_cls=RemovedInOscar20Warning):
    class Deprecated(cls):
        def __init__(self, *args, **kwargs):
            message = "Class '%s' is deprecated and will be " \
                "removed in the next version of JUS" \
                % cls.__name__
            warnings.warn(message, warn_cls, stacklevel=2)
            super(Deprecated, self).__init__(*args, **kwargs)
    return Deprecated
