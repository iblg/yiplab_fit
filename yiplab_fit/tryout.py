from open_read_csv import open_read_csv
from odr import odr_fit
import matplotlib.pyplot as plt
import numpy.random as rd
import numpy as np
from bg_mpl_stylesheet.bg_mpl_stylesheet import bg_mpl_style
plt.style.use(bg_mpl_style)



def main():

    files = {'Acetate': '/Users/ianbillinge/Documents/yiplab/projects/tsse/oxyanions/naac/sodium acetate dipa equil - export_org_25C.csv',
             'Sulfate':'/Users/ianbillinge/Documents/yiplab/projects/tsse/oxyanions/na2so4/SS_25C_equil/sodium sulfate dipa equil - export_org_25C.csv',
             'Nitrate': '/Users/ianbillinge/Documents/yiplab/projects/tsse/oxyanions/nano3/NaNO3_25C_equil/sodium nitrate dipa equil - export_org_25C.csv',
             'Phosphate': '/Users/ianbillinge/Documents/yiplab/projects/tsse/oxyanions/na3po4/sodium phosphate dipa equil - export_org_25C.csv',
             'Chloride': '/Users/ianbillinge/Documents/yiplab/projects/tsse/oxyanions/nacl/NaCl_25C_equil/sodium chloride dipa equil - export_org_25C.csv',
             'Carbonate': '/Users/ianbillinge/Documents/yiplab/projects/tsse/oxyanions/na2co3/sodium carbonate dipa equil - export_org_25C.csv'}

    fig, ax = plt.subplots()

    for key, file in files.items():
        data = open_read_csv(file)
        x = np.array(np.log10(data['x_{water}']).dropna())
        y = np.array(np.log10(data['x_{salt}']).dropna())
        print('\n {}'.format(key))
        fit_res = odr_fit(x, y, pprint = True)

        ax.plot(x,y, '.', label = key)
        xx = np.linspace(x.min(),x.max(), 10)
        yy = xx * fit_res.beta[0] + fit_res.beta[1]

        ax.plot(xx, yy, color = '#cccccc')

    ax.legend()
    plt.show()


    return


if __name__ == '__main__':
    main()