#!/usr/bin/env python
import sys
import os
import pysam


__author__ = "chao ning"
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley", "Matthew Wakefield"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "chao ning"
__email__ = "ningch@big.ac.cn"
__status__ = "Production"
__year__ = '2017'

if len(sys.argv) == 1:
	print sys.argv[0],'sam|bam'
	exit()



infor,length,reads_num = {},{},0
samfile = pysam.AlignmentFile(sys.argv[1], "rb")

for each in samfile.header:
	for line in samfile.header[each]:
		if 'SN' in line and 'LN' in line:
			length[line['SN']] = int(line['LN'])
for read in samfile:
	if read.is_read1 and read.mapping_quality > 10 :
		if read.reference_name not in infor:
			infor[read.reference_name] = 0
		infor[read.reference_name] += 1
		reads_num += 1

for each in infor:
	sys.stdout.write('\t'.join([str(i) for i in each,(infor[each] * 1000000 * 1000.0 ) / (reads_num * length[each])]) + '\n')
