from psychopy import core, data, gui, parallel, visual


# Experience Config
class Config:
    TEST = True
    WIDTH = 1920
    HEIGHT = 1080
    BACKGROUND_COLOR = [227, 227, 227]
    FONT = 'DejaVu Sans'
    PORT = '/dev/parport0'
    CONDITIONS = 'condition.csv'
    TEST_CONDITIONS = 'test_condition.csv'
    RESOURCE_DIR = 'pic'


# Test setting
if Config.TEST:
    Config.CONDITIONS = Config.TEST_CONDITIONS

# Collect subject information
sub_info = {'name': '', 'id': '', 'gender': ['male', 'female']}
inputDlg = gui.DlgFromDict(dictionary=sub_info, title='collect information', order=['name', 'id', 'gender'])

# Import trial conditions
conditions = data.importConditions(Config.CONDITIONS)
trials = data.TrialHandler(conditions, nReps=1, method='random')

# Run the experience
win = visual.Window([Config.WIDTH, Config.HEIGHT], color=Config.BACKGROUND_COLOR, units='pix')
# Start trial
for thisTrial in trials:
    # Show faces
    face = visual.ImageStim(win, image='img/' + thisTrial['image'], mask='circle', size=[800, 800])
    face.draw()

    # Show texts
    if thisTrial['text'] == 3:
        texts = visual.TextBox2(win, text='Smile', font=Config.FONT, pos=(300, 0), letterHeight=100, color=(0, 0, 0))
    else:
        texts = visual.TextBox2(win, text='Frown', font=Config.FONT, pos=(300, 0), letterHeight=100, color=(0, 0, 0))
    texts.draw()

    if not Config.TEST:
        # prepare the EEG device
        port = parallel.ParallelPort(Config.PORT)
        port.setData(0)

    win.flip()
    core.wait(2)

# Save result file
trials.saveAsExcel(fileName='testData', sheetName='rawData', stimOut=['image', 'text'])
