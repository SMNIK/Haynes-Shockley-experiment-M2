# Haynes-Shockley experiment (Module 2)
> [Haynes-Shockley-experiment-M1](https://github.com/SMNIK/Haynes-Shockley-experiment-M1) <br>
> The charge mobility in semiconductor materils.

It was the first experiment to measure directly the drift velocity, and thus mobility, of minority carriers. Previously the drift velocity was determined with the Hall effect, which was an direct method whose results could not be easily interpreted.
In the original H-S experiment an electric field is created along a small bar of a doped semiconductor (cut from a single crystal ingot) by applying an experimental voltage across the bar ends. Then a short pulse injects excess minority charge carriers into the sample which are successively swept along the bar by the electric field. By detecting and analyzing the excess-charge pulse during its travel, the drift velocity, the diffusion constant and lifetime may be calculated.
>
>#### More Study
><a href="https://www.labtrek.it/haynes-shockley-experiment/">labtrek</a><br>
><a href="https://aip.scitation.org/doi/pdf/10.1063/1.334081">aip.scitation.org
></a>
>### Goals
>- Minority charge carrier amount.
>- the effect of the distance electrodes on the production of electrons and 
>holes.
>- measuring of carrier's lifetime.

![image](./image/image.jpg)
>Block diagram for optical injection and point-contact collector

Important fields are: ***lifetime, drift velocity, electric field***

<h3>Measurement of the time of flight t</h3>
<p> Due to the constant of the distance and the moving fields, the flight time is also constant, which does not depend on the density of the laser pulse. so the spectrom just increases the peak of the graph relevant to the voltage. Despite the fact that t is grown by increasing inject charge density.</p>

On the oscilloscope screen we may observe a first short negative pulse, with amplitude comparable to that of the injection pulse V<sub>I</sub> and, after some delay t, a second negative pulse, wider and much smaller than the first one. An example of the collected signal in a <em>N-doped</em> Ge sample, with posittive injecting and sweep pulses is shown below (here the excess injected carriers are holes, not electrons). 

![image](./image/flight-peaks.png)


The first peak is simultaneous with the injection pulse: it is due to the electromagnetic signal propagating across the sample. The second pulse (the top plot) corresponds to the excess-charge distribution passing under the collector contact: its shape is approximately <a href="https://en.wikipedia.org/wiki/Gaussian_function"><em>Gaussian</em></a> and its amplitude and width are determined by diffusion and recombination processes.
An analytical interpretation of the pulse shape, based on the solution of the time dependent diffusion equation, may be found in Gaussian coefficients. 

<h3>Measurment of drift velocity</h3>
<p>
  E<sub>s</sub> is an internal electric pulse field that produced by a pulsed generator. Distance between optical fiber and needle (<ins>point contact</ins>) is <em>d</em>.  V<sub>s</sub> is the electrical pulls and V<sub>l</sub> is the laser pulls. The lasr pulls causes 2 small peak between up and down main semiconductor peak. The second peak is the wider and relevant to minority carriers.
</p>

<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h3>Information that can be extracted from the pulse shape and position</h3>
  <table>
    <tr>
      <td>the drift velocity</td>
      <td><a href="https://www.codecogs.com/eqnedit.php?latex=V_{d}=\frac{d}{t}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V_{d}=\frac{d}{t}" title="V_{d}=\frac{d}{t}" /></a></td>
    </tr>
      <tr>
    <td>sweep field (L : sample length)</td>
    <td><a href="https://www.codecogs.com/eqnedit.php?latex=E_{s}=\frac{V_{s}}{L}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_{s}=\frac{V_{s}}{L}" title="E_{s}=\frac{V_{s}}{L}" /></a></td>
  </tr>
    <tr>
        <td>so electron mobility is</td>
        <td><a href="https://www.codecogs.com/eqnedit.php?latex=\mu&space;=\frac{|V_{d}|}{|E_{s}|}=\frac{Ld}{t&space;V_{s}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mu&space;=\frac{|V_{d}|}{|E_{s}|}=\frac{Ld}{t&space;V_{s}}" title="\mu =\frac{|V_{d}|}{|E_{s}|}=\frac{Ld}{t V_{s}}}" /></a></td>
    </tr>
    <tr>
        <td>then relation of Diffusion and collected pulse</td>
        <td><a href="https://www.codecogs.com/eqnedit.php?latex=(\Delta&space;t\&space;V_{d})^{2}=16&space;\&space;ln(2Dt)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(\Delta&space;t\&space;V_{d})^{2}=16&space;\&space;ln(2Dt)" title="(\Delta t\ V_{d})^{2}=16 \ ln(2Dt)" /></a></td>
  </tr>
</table>
<p> The semiconductor sample is a thin bar (approximately 3x3x30 mm) of single crystal ingot.</p>

<div>
<em>photo electric effect (LASER beam) causes the drift mobility of minority charge carriers sweeps length of the semiconductor.</em><br>
The excess charges may be generated by a light pulse (by exploiting the internal photoelectric effect) e.g. using a beam, produced by LASER diode, and the emitted light beam is guided by an optical fiber with one end replacing the emitter point contact.


</div>
<hr>
</body>
</html>

# Project Structure
The below configuration, explains how to use the codes and change them for your data:
> the 3 simple steps

1) The first step is the preparation excel file as the x and y column header.Then, plot your data by calling matplot library ([plotting.py](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/plotting.py)). 
2) The plot shows us the peak of minority mobility of sample which the scale is voltage per time. As we know, these data involves noises and we need to excract the usful data. Use one of the fit configurations and calculate the coefficients. Then, for fitting configuration you should launch the plotting.py inside the fitPlot.py for importing data for your fit. Here I used the [Gaussian](https://en.wikipedia.org/wiki/Gaussian_function) fit inside the [fitPlot.py](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/fitPlot.py).
3) Finally, users should use the above files for as many he wants to plot and calculates the coefficients. Finally, for each voltage creat plotting and fitPlot, and launch your different lists inside the ***coefficientsTable*** for plotting them. As, I do inside the [testing.py](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/testing.py). 

***Parts of my code***
- The [plottin.py](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/plotting.py) reads your excel file and extracts data for plotting. If you want to have different plots for different voltages, you should add more sheets names and plot them. For example:
```python
# first = pd.read_excel(<address and name of your file>,<name of the sheet>)
first = pd.read_excel(r'Book1.xlsx', '14.4v')
second = pd.read_excel(r'Book1.xlsx', '20.9v')
# x = first['<name of the column>'][<index from>:<to>]
x_1 = first['x'][500:4000]
y_1 = first['y'][500:4000]

x_2 = second['x'][500:4000]
y_2 = second['y'][500:4000]

plt.plot(x_1,y_1)
plt.plot(x_2,y_2)
```
And the same, change the coefficients' names, and change the x & y inside the fitPlot to x_1 & y_1 and repeat the gaussian for the second one and so on. Or, you can prepare different files for each voltage (for example fit1.py, fit2.py,... and the same for the next files). Just be careful, by choosing as each way the launch process should be changed inside the next files.
 You could use the [Module 1](https://github.com/SMNIK/Haynes-Shockley-experiment-M1), however, in conclusion I will explaine the differences.
- As we know, in this experiment, data contains noise of staffs, so, we need to prepare the fit result as the new data for calculating the mobility, mean free path, and fly time. From [fitPlot.py](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/fitPlot.py), call your data and then you can fit the peaks by Gaussian method and extract the coefficients for calculation. As I said above, for each voltage you should be careful for launching.
- And in [coefficientsTable.py](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/coefficientsTable.py), call the coefficients, check if the name of sheet is true, prepare the new excel file and extract your fit's data in different index. And, plot the logarithmic Area per time to modify the fit line for different voltage.
- In [testing.py](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/testing.py), I call all my sheets and for each List I use different index. Finally, arrange your table and plot the last figure which I explaine in the above part.

## Conclusion

> differences between M1 and M2 are : 
> in M1 you should calculate each voltage in seperat file, but M2 calculate all sheets (voltages) in on touche.
> because of seperating files in M1, you can change each part as you prefer, but in M2 may be appeares error.
> M1 is a sample of how the libraries in python work, for example we call plotting inside the fitPlot. However, in M2 it is not the same. The benefites of this method is that may be our library would be useful for other users.
> [Module 1](https://github.com/SMNIK/Haynes-Shockley-experiment-M1)

***At the end some results***

![image](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/image/peaks-and-fits.png)

![image](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/image/analyses.png)

![image](https://github.com/SMNIK/Haynes-Shockley-experiment-M2/blob/master/image/t-lnA.png)