"""
Importer for PubTator data
"""

import kindred
import requests

def _loadPMID(pmid):
	assert isinstance(pmid,int)
	
	annotationsURL = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/BioConcept/%d/JSON" % pmid
	
	annotations = requests.get(annotationsURL).json()
	doc = kindred.loadFunctions.parseJSON(annotations)
	
	return doc

def load(pmids):
	"""
	Load a set of documents with annotations from Pubmed given a list of Pubmed IDs (PMIDs)
	
	>>> corpus = load(19894120)
	>>> len(corpus.documents)
	1

	:param pmids: the list of Pubmed IDs
	:type pmids: List of ints
	:returns: a kindred corpus object
	:rtype: kindred.Corpus
	"""

	assert isinstance(pmids,list) or isinstance(pmids,int)

	corpus = kindred.Corpus()
	if isinstance(pmids,list):
		for pmid in pmids:
			doc = _loadPMID(pmid)
			assert isinstance(doc,kindred.Document)
			corpus.addDocument(doc)
	elif isinstance(pmids,int):
		doc = _loadPMID(pmids)
		assert isinstance(doc,kindred.Document)
		corpus.addDocument(doc)
	return corpus
	
	
	
	
