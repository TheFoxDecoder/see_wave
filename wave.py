# !/bin/usr/fuck
import librosa

class see_wave:
    def __inti__(self,file_name):
        self.file_name =

    def tip_spectrogram(self):
        # getting information from the file
        time_series, sample_rate = librosa.load(self.file_name)
        # getting a matrix which contains amplitude values according to frequency and time indexes
        stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))
        # converting the matrix to decibel matrix
        spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

    def view_sepctorgram(self):
        librosa.display.specshow(self.spectrogram,
                            y_axis='log', x_axis='time')
        plt.title('Your title')
        plt.colorbar(format='%+2.0f dB')
        plt.tight_layout()
        plt.show()
    def run():
        tip_spectrogram()
        view_sepctorgram()

if __name__ == '__main__':
    
    

