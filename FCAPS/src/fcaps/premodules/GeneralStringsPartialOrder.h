#ifndef GENERALSTRINGSPARTIALORDER_H
#define GENERALSTRINGSPARTIALORDER_H

#include <SimpleStringsPartialOrder.h>

////////////////////////////////////////////////////////////////////

typedef CStringsPartialOrderElement< CSharedPtr<IPatternDescriptor> > CGeneralStringsPartialOrderElement;

class CGeneralStringsPartialOrderComparator : public CStringsPartialOrderComparator< CSharedPtr<IPatternDescriptor> > {
public:
	typedef CSharedPtr<IPatternDescriptor> TElem;
public:
	CGeneralStringsPartialOrderComparator()
		{}

	// Set comparator of elements in strings.
	void Initialize( const CSharedPtr<IPatternDescriptorComparator>& _elemsCmp )
		{ elemsCmp = _elemsCmp; assert(elemsCmp != 0); }

protected:
	// Methods of CStringsPartialOrderComparator
	virtual void PreprocessStrElem( const TElem& el ) const;
	virtual TCompareResult CompareElems( DWORD cmpMask, const TElem& first, const TElem& last ) const;
	virtual TElem CalculateElemsSimilarity( const TElem& first, const TElem& last ) const;
	virtual bool IsMostGeneralElem( const TElem& el ) const;
	virtual void WriteElem( const TElem& el, std::ostream& dst ) const;

private:
	CSharedPtr<IPatternDescriptorComparator> elemsCmp;
};

#endif // GENERALSTRINGSPARTIALORDER_H