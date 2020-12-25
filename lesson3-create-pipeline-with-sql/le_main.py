import luigi
from le_export_data import *


class MainTask(luigi.WrapperTask):
    def requires(self):
        print("=======>1. MainTask")
        return ExportAllQueries()


if __name__ == '__main__':
    luigi.run(main_task_cls=MainTask, local_scheduler=True)
