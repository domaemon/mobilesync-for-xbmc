import sys, os, re, shutil
import xbmc, xbmcgui

woman = {}
woman['to_dir'] = '/media/4b65836d-6b9a-47e9-b452-363f2e722f93/Koti'
woman['from_dir'] = '/media/Nokia N9/DCIM/'
woman['postfix'] = "_n"

man = {}
man['to_dir'] = '/media/4b65836d-6b9a-47e9-b452-363f2e722f93/Koti'
man['from_dir'] = '/media/Nokia N9/DCIM'
man['postfix'] = '_m'

profile_ptr = {}

profiles = {'woman': woman, 'man': man}

if ( __name__ == "__main__" ):
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Choose a profile', ['woman', 'man'])

    if (ret == 0):
        profile_ptr = woman;
    elif (ret == 1):
        profile_ptr = man;
    
    from_files = []
    from_files = os.listdir(profile_ptr['from_dir']);
    progress_denominator = len(from_files);
    progress_numerator = 0;
    progress_percent = 0

    dialog_progress = xbmcgui.DialogProgress()
    ret = dialog_progress.create('XBMC', 'mobilesync', 'sync in progress');

    for file in from_files:
        progress_numerator = progress_numerator + 1;
        progress_percent = int(float(progress_numerator) / float(progress_denominator) * 100);
        dialog_progress.update(progress_percent, file)
        
        m = re.match("((\d{6})\d{2}_\d{3}).(\w{3})", file);

        if (m):
            if (m.group(3) == "jpg"):
                to_dir = os.path.join(profile_ptr['to_dir'], "MyPictures", m.group(2));
            elif (m.group(3) == "mp4"):
                to_dir = os.path.join(profile_ptr['to_dir'], "MyVideos", m.group(2));

            to_file = os.path.join(to_dir, m.group(1) + profile_ptr['postfix'] + "." + m.group(3));
            from_dir = profile_ptr['from_dir']
            from_file = os.path.join(from_dir, file)
        
            if (not os.path.exists(to_dir)):
                print "making directory", to_dir, "..."
                os.mkdir(to_dir, 0755) 
            
        # if the to_file does not exist..
            if (not os.path.isfile(to_file)):
                shutil.copy(from_file, to_file);

dd
