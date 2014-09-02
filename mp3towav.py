def processMp3File(filePath, filename, outputPath=None):
    if filename.endswith('.mp3'):
        # execute code
        ffmpeg = r'C:\Users\wgillis\Downloads\ffmpeg-20140829-git-4c92047-win64-static\bin\ffmpeg.exe'
        import subprocess, os
        if not outputPath:
            outputPath = filename[:-4] + '.wav'
        else:
            outputPath = os.path.join(outputPath, filename[:-4] + '.wav')
        args = [ffmpeg, '-i', os.path.join(filePath, filename) , outputPath]
        subprocess.call(args, shell=True)
        return outputPath

    else:
        print('Isn\'t mp3 file!')
        return False