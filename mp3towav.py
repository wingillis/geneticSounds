# TODO: add support for both linux and windows systems
# make sure that the user also has ffmpeg installed 
def processMp3File(filePath, filename, outputPath=None):
    if filename.endswith('.mp3'):
        # execute code
	# User defined location for ffmpeg
        ffmpeg = r'C:\Users\wgillis\Downloads\ffmpeg-20140829-git-4c92047-win64-static\bin\ffmpeg.exe'
        linuxModule = 'avconv'
        import subprocess, os, sys
        if not outputPath:
            outputPath = filename[:-4] + '.wav'
        else:
            outputPath = os.path.join(outputPath, filename[:-4] + '.wav')

        args = [ffmpeg, '-i', os.path.join(filePath, filename) , outputPath]
        if sys.platform == 'linux':
            args[0] = linuxModule

        subprocess.call(args, shell=True)
        return outputPath

    else:
        print('Isn\'t mp3 file!')
        return False
