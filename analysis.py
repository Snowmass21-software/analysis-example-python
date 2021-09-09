import uproot
import hist
import awkward as ak

jetMass = hist.Hist(hist.axis.Regular(40, 0, 1000, name="x"))

for batch in uproot.iterate(
    "/collab/project/snowmass21/data/smmc/v0.1/r1/100TeV_B.tar.gz/delphesstep/*.root:Delphes",
    filter_name="Jet.Mass",
):
    mask = ak.num(batch["Jet.Mass"]) > 0
    jetMass.fill(batch["Jet.Mass"][mask][:, 0])

jetMass.show(columns=50)
