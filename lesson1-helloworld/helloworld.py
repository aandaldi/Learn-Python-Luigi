import luigi

class HelloWorld(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('helloworld.txt')
    
    def run(self):
        with self.output().open('w') as outfile:
            outfile.write('Hello World!\n')

#Targets are some sort of data that is persisted between task runs.
# HellIn this tutorial we will only work with luigi.LocalTarget()'s, which are normal files.


if __name__ == "__main__":
    luigi.run()