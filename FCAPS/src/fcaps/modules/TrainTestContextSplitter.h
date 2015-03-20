#ifndef CTRAINTESTCONTEXTSPLITTER_H
#define CTRAINTESTCONTEXTSPLITTER_H

#include <fcaps/Filter.h>
#include <fcaps/Module.h>

#include <rapidjson/document.h>

////////////////////////////////////////////////////////////////////

const char TrainTestContextSplitter[] = "TrainTestContextSplitter";

class CTrainTestContextSplitter : public IFilter, public IModule {
public:
	CTrainTestContextSplitter();
	// Methods of IFilter
	virtual const std::vector<std::string>& GetResultFiles() const
		{ return results; }
	virtual const std::string& GetInputFile() const
		 { return inputFile; }
	virtual void SetInputFile( const std::string& path )
		{ inputFile = path; }
	virtual void Process();

	// Methods of IModule
	virtual void LoadParams( const JSON& );
	virtual JSON SaveParams() const;

private:
	static const CModuleRegistrar<CTrainTestContextSplitter> registrar;
	// Resulting file (two files).
	std::vector<std::string> results;
	// The path to the input file.
	std::string inputFile;
	// The proportion between train and test datasets. Default 90% is the train set.
	double proportion;
	// Seed for the random
	int seed;

	rapidjson::Value data;
	rapidjson::Document params;
	rapidjson::Value objNames;

	void writeDataset(
		std::vector<int>::const_iterator b, std::vector<int>::const_iterator e,
		const std::string& path );
	void initObjectNames(std::vector<int>::const_iterator b, std::vector<int>::const_iterator e );
};

#endif // CTRAINTESTCONTEXTSPLITTER_H