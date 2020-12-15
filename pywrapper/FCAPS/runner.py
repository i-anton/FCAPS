import subprocess
import uuid
import json
import re
import os.path
from FCAPS.shared_utils import NoValue, ModuleSetting

class InfoLog(NoValue):
    ConsoleOut = 'COUT'
    ConsoleError = 'CERR'
    FileOut = 'File'


class Runner:
    write_param_file = None
    def setWriteParamFile(self, file: str):
        """ DEBUG: Set filename to log passed to Sofia-PS parameters """
        self.write_param_file = file
        return self

    param_file = None
    def setParamFile(self, file: str):
        """ Set path to file with one param per one line """
        self.param_file = file
        return self

    info_log = None
    def setInfoLog(self, method: InfoLog = InfoLog.FileOut, path: str = None):
        """ DEBUG: Set path for writing info log """
        if method == InfoLog.FileOut:
            self.info_log = path
        else:
            self.info_log = method.value
        return self

    time_limit = None
    def setTimeLimit(self, limit: int):
        """ Set run time limit """
        if limit <= 0:
            raise ValueError('Limit should be positive')
        if limit >= 2147483647:
            raise ValueError('Limit should be less than 2147483647')
        self.time_limit = limit
        return self

    context_processor = None
    def setFileContextProcessor(self, context_processor_new: str):
        """ Set path to params of Context Processor in JSON """
        self.context_processor = context_processor_new
        return self

    context_processor = None
    def setCustomContextProcessor(self, context_processor_new: ModuleSetting, filename: str ='myparams.json'):
        """ Set path to params of Context Processor in JSON """
        parameters = context_processor_new.to_dict()
        with open(filename, "w") as outfile:  
            json.dump(parameters, outfile, indent = 4)
        self.context_processor = filename
        return self

    filter_name = None
    def setFilter(self, filter_new: str):
        """ Path to params of the filter applied to the lattice """
        self.filter_name = filter_new
        return self

    modules_path = './modules/'
    def setModulesPath(self, path: str):
        """ Set path to folder with FCAPS modules (.dll) """
        self.modules_path = path
        return self

    output_path = None
    def setOutput(self, path: str):
        """ JSON file name with result (by default fcaps-result-{random_uuid()}.json """
        self.output_path = path
        return self

    def run(self) -> list:
        complete_args = ['Sofia-PS']
        if self.context_processor:
            complete_args.append(f"-CP:{self.context_processor}")
        else:
            raise ValueError('Context processor is required')
        if self.filter_name:
            complete_args.append(f"-fltr:{self.filter_name}")
        if self.write_param_file:
            complete_args.append(f"--writeparamfile:{self.write_param_file}")
        if self.param_file:
            complete_args.append(f"--paramfile:{self.param_file}")
        if self.info_log:
            complete_args.append(f"--infoLogging:{self.info_log}")
        if self.time_limit:
            complete_args.append(f"--timeLimit:{self.time_limit}")
        if self.modules_path:
            complete_args.append(f"-M:{self.modules_path}")
        outfile = self.output_path if self.output_path else f"fcaps-result-{uuid.uuid4().hex}.json"
        complete_args.append(f"-out:{outfile}")

        process = subprocess.run(complete_args, capture_output=True)
        if len(process.stderr) > 0:
            raise Exception(f'FCAPS encoutered errors: {process.stderr}')
        
        with open(outfile) as first_file:
            data = json.load(first_file)
        
        result = [data]

        selected_data = None
        selected_filename = re.sub(r'\.json$', '.selected.json', outfile)
        if os.path.isfile(selected_filename):
            with open(selected_filename) as selected_file:
                selected_data = json.load(selected_file)
        
        if selected_data is not None:
            result.append(selected_data)
        return result
        # process = subprocess.run(['Sofia-PS', '--silent'])

# subprocess.check_call([r"C:\pathToYourProgram\yourProgram.exe", "your", "arguments", "comma", "separated"])
