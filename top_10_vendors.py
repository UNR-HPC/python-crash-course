from csv import DictReader, writer
from operator import itemgetter
from optparse import OptionParser

def get_vendor_amounts(file_name):
	vendor_amounts = {}
	with open(file_name, 'rb') as checkbook:
		checkbook_reader = DictReader(checkbook)
		for row in checkbook_reader:
			if row['VENDORNAME'] in vendor_amounts:
				vendor_amounts[row['VENDORNAME']] += float(row['AMOUNT'])
			else:
				vendor_amounts[row['VENDORNAME']] = float(row['AMOUNT'])
	
	return vendor_amounts

def get_top_ten_va(vendor_amounts):
	sorted_vendor_amounts = sorted(vendor_amounts.items(), key=itemgetter(1), reverse=True)
	return sorted_vendor_amounts[:10]


def write_top_ten(file_name, top_ten):
	with open(file_name, 'wb') as va_file:
		va_writer = writer(va_file, delimiter=',')

		va_writer.writerow(['Vendor', 'Amount'])
		for va in top_ten:
			va_writer.writerow(va)

def main(in_file_name, out_file_name):
	vendor_amounts = get_vendor_amounts(in_file_name)
	top_ten = get_top_ten_va(vendor_amounts)
	write_top_ten(out_file_name, top_ten)

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('-i', '--infile', dest='in_file_name')
	parser.add_option('-o', '--outfile', dest='out_file_name')

	(options, args) = parser.parse_args()

	if options.in_file_name is None:
		raise ValueError("Input file name cannot be None. Please set -i option.")

	if options.out_file_name is None:
		raise ValueError("Output file name cannot be None. Please set -o option.")

	main(options.in_file_name, options.out_file_name)