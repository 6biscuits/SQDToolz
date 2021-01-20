from sqdtoolz.Experiment import Experiment
from sqdtoolz.HAL.DDG import*
from sqdtoolz.TimingConfiguration import*

new_exp = Experiment(instr_config_file = "tests\\BenchTest.yaml", save_dir = "", name="test")

#Can be done in YAML
# instr_ddg = DDG_DG645('ddg_real')
# new_exp.add_instrument(instr_ddg)

#Ideally, the length and polarity are set to default values in the drivers via the YAML file - i.e. just set TrigPulseDelay
ddg_module = DDG(new_exp.station.load_pulser())
ddg_module.get_trigger_output('AB').TrigPulseLength = 50e-9
ddg_module.get_trigger_output('AB').TrigPolarity = 1
ddg_module.get_trigger_output('AB').TrigPulseDelay = 10e-9
ddg_module.get_trigger_output('CD').TrigPulseLength = 100e-9
ddg_module.get_trigger_output('CD').TrigPulseDelay = 50e-9
ddg_module.get_trigger_output('CD').TrigPolarity = 1
ddg_module.get_trigger_output('EF').TrigPulseLength = 400e-9
ddg_module.get_trigger_output('EF').TrigPulseDelay = 250e-9
ddg_module.get_trigger_output('EF').TrigPolarity = 0


# awg.set_trigger_source(ddg_module.get_trigger_source('A'))

tc = TimingConfiguration(1e-6, [ddg_module])
lePlot = tc.plot().show()
input('press <ENTER> to continue')





# ddg_module._instr_ddg.CD.trigPulseLength(float(500e-9))
# ddg_module._instr_ddg.write_raw('DLAY 5,4,7e-07\n')



# import visa
# rm = visa.ResourceManager()
# rm.list_resources()
# ('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::14::INSTR')
# my_instrument = rm.open_resource('GPIB0::14::INSTR')
# print(my_instrument.query('*IDN?'))
