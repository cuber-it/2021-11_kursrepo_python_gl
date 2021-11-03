import sys
#import log_reader as lr
import log_read_class as lrc

if len(sys.argv) != 3:
    print("usage: log_reader input_logfile_name output_logfile_name")
    exit(1)

infname = sys.argv[1]
outfname = sys.argv[2]

#raw_data = lr.read_file(infname)
#cooked_data = lr.cleanup_log(raw_data)
#lr.write_file(outfname, cooked_data)

log_reader = lrc.LogReader(infname, outfname)
log_reader.read_file()
log_reader.cleanup_log()
log_reader.write_file()

exit(0)