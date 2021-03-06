import calendar
from datetime import datetime
from .Insurance.maths376 import maths_376
from .Insurance.maths377 import maths_377
from .Insurance.maths378 import maths_378
from .Reinsurance.maths404 import maths_404
from .Reinsurance.maths405 import maths_405
from .Reinsurance.maths406 import maths_406
from .Reinsurance.maths407 import maths_407
from .Reinsurance.maths408 import maths_408
from .Reinsurance.maths409 import maths_409


class maths:

    def __init__(self, year, qe):
        self.qe = qe
        self.dates_seguros = [datetime(year, month, calendar.monthrange(
            year, month)[1]).strftime("%Y%m%d")for month in range(1, 13)]
        self.dates_reseguros = [
            f"{year}" + f"{month}".zfill(2) for month in range(1, 13)]
        if self.qe == 376:
            self.math = maths_376(self.dates_seguros)
        elif self.qe == 377:
            self.math = maths_377(self.dates_seguros)
        elif self.qe == 378:
            self.math = maths_378(self.dates_seguros)
        # Reinsurance
        elif self.qe == 404:
            self.math = maths_404(self.dates_reseguros)
        elif self.qe == 405:
            self.math = maths_405(self.dates_reseguros)
        elif self.qe == 406:
            self.math = maths_406(self.dates_reseguros)
        elif self.qe == 407:
            self.math = maths_407(self.dates_reseguros)
        elif self.qe == 408:
            self.math = maths_408(self.dates_reseguros)
        elif self.qe == 409:
            self.math = maths_409(self.dates_reseguros)
        # Capitalization
        elif self.qe in [419, 420, 421, 422, 423]:
            pass
        
    def score_line(self, line):
        if self.qe not in [419, 420, 421, 422, 423]:
            self.math.run(line)
                
    def get_dataframe(self):
        return self.math.df