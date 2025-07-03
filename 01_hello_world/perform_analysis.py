import logging
import os
import time
import random 

from pbprocesstools.pbpt_q_process import PBPTQProcessTool

logger = logging.getLogger(__name__)


class ProcessCmd(PBPTQProcessTool):
    def __init__(self):
        super().__init__(cmd_name="perform_analysis.py", descript=None)

    def do_processing(self, **kwargs):
    
        # Note you access the variables specified in the gen_cmds.py
        # script by using the self.params directionary
        # e.g., self.params["output_file"]
    
        out_text = "Hello World - {}".format(self.params["n"])
        
        # An error will be thrown on job 3 to illustrate 
        # how pb_process_tools catches errors.
        if self.params["n"] == 3:
            raise Exception("n == 3 so throwing an error")
        
        f = open(self.params["output_file"], "w")
        f.write(out_text + "\n")
        f.flush()
        f.close()
        
        # Wait a random time between 5 and 20 secs
        # You do not need this but it means the jobs
        # will take a little longer to run so you can  
        # use the run_report.sh script to see progress
        slp_time = random.randint(5, 20)
        print(f"Sleeping for {slp_time}")
        time.sleep(slp_time) 
        print("Finished")

    def required_fields(self, **kwargs):
        # Return a list of the required fields which will be checked
        return [
            "n",
            "output_file",
        ]

    def outputs_present(self, **kwargs):
        # Check the output files are as expected - called with --check option
        # the function expects a tuple with the first item a list of booleans
        # specifying whether the file is OK and secondly a dict with outputs
        # as keys and any error message as the value

        # A function (self.check_files) has been provided to do the work for
        # you which takes a dict of inputs which will do the work for you in
        # most cases. The supported file types are: gdal_image, gdal_vector,
        # hdf5, file (checks present) and filesize (checks present and size > 0)

        files_dict = dict()
        files_dict[self.params["output_file"]] = "file"
        return self.check_files(files_dict)

    def remove_outputs(self, **kwargs):
        # Remove the output files and reset anything
        # else which might need to be reset if re-running the job.
        if os.path.exists(self.params["output_file"]):
            os.remove(self.params["output_file"])


if __name__ == "__main__":
    ProcessCmd().std_run()

