from csv import DictReader, writer
from optparse import OptionParser

def get_vendors(file_name):
	if file_name is None:
		raise ValueError("file_name cannot be None")

	vendors = set()
	with open(file_name, 'rb') as checkbook:
		checkbook_reader = DictReader(checkbook)
		for row in checkbook_reader:
			vendors.add(row['VENDORNAME'])

	return vendors

def write_vendors(file_name, vendors):
	if file_name is None:
		raise ValueError("file_name cannot be None")
	if vendors is None:
		raise ValueError("vendors cannot be None")

	with open(file_name, 'wb') as vendor_file:
		vendor_writer = writer(vendor_file, delimiter=',')

		for vendor in vendors:
			vendor_writer.writerow([vendor])

def main(in_file_name, out_file_name):
	if in_file_name is None:
		raise ValueError("in_file_name cannot be None")
	if out_file_name is None:
		raise ValueError("out_file_name cannot be None")

	vendors = get_vendors(in_file_name)
	print 'Reno paid %d vendors' % len(vendors)
	write_vendors(out_file_name, vendors)

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('-i', '--infile', dest='in_file_name')
	parser.add_option('-o', '--outfile', dest='out_file_name')

	(options, args) = parser.parse_args()

	main(options.in_file_name, options.out_file_name)