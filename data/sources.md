# Sources and figure audit trail

Every number in the brief traces to an entry below: value, unit as printed, document, publisher, date, and location in the document. Conversions are shown where the brief or charts restate a figure in different units. All sources were accessed October 12, 2026. Downloaded PDFs are archived in the project working files.

## Conversion factors used

- 1 US gallon = 3.78541 liters
- 1 cubic meter = 1,000 liters = 264.172 US gallons
- 1 megaliter = 1,000,000 liters = 264,172 US gallons
- Billion gallons per day to billion liters per year: multiply by 365 x 3.78541

## Definitions the brief never mixes without labels

- Withdrawal: water taken from a source. Some of it is returned (discharge).
- Consumption: water withdrawn and not returned, mostly evaporated in cooling.
- Direct (onsite, scope 1): water used at the data center itself.
- Indirect (scope 2): water consumed generating the electricity the data center buys.

## S1. LBNL, 2024 United States Data Center Energy Usage Report

- Document: "2024 United States Data Center Energy Usage Report", Lawrence Berkeley National Laboratory, report LBNL-2001637, December 2024. Publisher site: eta.lbl.gov.
- Electricity use 2018: about 76 TWh, 1.9% of total US electricity consumption. Executive summary and Section 5.
- Electricity use 2023: 176 TWh, 4.4% of total US electricity consumption. Executive summary and Section 5.
- Electricity use 2028, projection range: roughly 325 to 580 TWh, 6.7% to 12.0% of forecast US electricity consumption, at 50% utilization 74 to 132 GW of power capacity. Executive summary, Figure ES-1; Section 5, Figure 5.5.
- Direct water consumption 2014: 21.2 billion liters, 64% in internal (enterprise) data centers. Section 5, "Direct Water Consumption", p. 55.
- Direct water consumption 2023: 66 billion liters total; hyperscale plus colocation = 84% of the total. Same section, p. 55.
- Direct water consumption 2028: hyperscale data centers alone projected at 60 to 124 billion liters. Same section, pp. 55-56. No all-segment 2028 total is printed in this passage, and the brief does not invent one.
- Indirect water consumption 2023: nearly 800 billion liters, consumed through electricity use. Section 5, "Indirect Water Consumption and Emissions from Electricity Use", p. 57.
- Indirect water intensity 2023: national average 4.52 L/kWh for data center electricity, vs. 4.35 L/kWh average for US electricity overall. Same section, p. 57.
- GHG emissions 2023 (electricity): 61 billion kilograms CO2 equivalent. Same section, p. 57.
- Average PUE: falls from 1.6 in 2014 to 1.4 in 2023; hyperscale and colocation under 1.4 by 2023. Section 4, Figure 4.6 discussion, pp. 47-48.
- Classification: bucket 2 (modeled estimates by a credible body with a stated method). The report is a model built on shipment, survey, and metered data, not a census of meter readings.

## S14. LBNL, United States Data Center Energy Usage Report: 2025 Update

- Document: "United States Data Center Energy Usage Report: 2025 Update", Lawrence Berkeley National Laboratory, report LBNL-2001758, June 2026. Authors: Sarah J. Smith, Alex Hubbard, Alex Newkirk, Mohan Ganeshalingam, Billie Holecek, Dale Sartor, Michael Mills, and Arman Shehabi. Prepared for the US Department of Energy. Hosted on eScholarship (University of California): https://escholarship.org/uc/item/33m6w3x0, DOI 10.71468/P1RP4F. PDF archived in the project working files (src/lbnl_2025_update.pdf). This report updates S1 and supersedes its 2028 outlook; it does not supersede S1's water figures (see the water note at the end of this entry).
- Method: the same bottom-up energy model as S1, with updated IT equipment shipment data (through late 2025), non-commercial ASIC accelerators added, updated AI server wattages, and revised AI inference power assumptions. Section 1 (executive summary) and Section 2.
- Electricity use 2024: 192 TWh, 4.7% of total US electricity consumption. The report notes this falls at the low end of the range S1 projected. Section 2, "Total Energy Use", p. 7.
- Historical revision: the update's estimates for prior years fall slightly below S1's, mainly due to a reduction in reported GPU shipments for 2023 and 2024 and revised AI inference server power assumptions. Same passage, p. 7. The update does not print a revised 2023 TWh total in its text; its Figure 1 (p. 7) plots the revised 2016-2024 series.
- Growth rates as printed: a 14% increase in US data center electricity use between 2023 and 2024; Reference Case growth of 22% from 2024 to 2025 and 29% from 2025 to 2026, then a compound annual growth rate of 21%. Section 4 (Conclusion), p. 25. Note the arithmetic the text implies: 14% growth to 192 TWh means the update's revised 2023 value is about 168 TWh (derived: 192 / 1.14 = 168.4), not S1's 176 TWh. The brief therefore keeps 2023 labeled with S1's published figure and never presents 176-to-192 as a 14% increase.
- Electricity use 2028, Reference Case: 464 TWh, which the report notes falls in the middle of S1's 325 to 580 TWh range. Section 2, p. 7.
- Electricity use 2030, Reference Case: 649 TWh, 11.8% of forecasted 2030 US electricity (forecast basis: NERC's 2025 Long-Term Reliability Assessment). Section 1, p. 4; Section 2, Table 2, p. 8.
- Electricity use 2030, Sensitivity Scenarios (Table 2, p. 8): Consolidated Deployment (GPU and ASIC shipments lowered 15%): 578 TWh, 10.5%. High ASIC (ASIC shipments raised 15%): 664 TWh, 12.1%. Low Accelerator Lifetime (average AI accelerator operating lifetime reduced by one year): 590 TWh, 10.7%. High Inference Energy (higher AI server idle power and utilization for inference workloads): 782 TWh, 14.2%.
- Electricity use 2030, Compounded Uncertainty range: 521 to 843 TWh, 9.5% to 15.3% of forecast US electricity. Section 1, p. 5; Table 2, p. 8.
- Share of load growth: in the Reference Case, data centers are responsible for 33% of total US load growth from 2024 to 2030 (against the NERC forecast). Section 2, p. 7.
- Power capacity 2030, Reference Case: 148 GW of interconnection capacity at an assumed 50% average utilization rate; an average increase of 17.4 GW per year from 2024 to 2030 (a 22% compound annual growth rate). Section 2, pp. 8-9.
- Aggregate PUE: reaches 1.36 in 2030 in the Reference Case. Section 3, p. 24.
- WATER: the update contains no water-use estimates. The word "water" appears only in passing (the Conclusion, p. 26, names water resources among the constraints future research should characterize; a front-matter services listing), and no withdrawal, consumption, or WUE figure appears anywhere in the document. All water figures in the brief therefore remain S1's (December 2024), still the most recent LBNL water assessment.
- Classification: bucket 2 (same modeled method as S1, updated inputs).

## S2. Google Environmental Reports (2025 and 2026 editions)

- Documents: "Environmental Report 2025" (calendar 2024 data) and "Environmental Report 2026" (calendar 2025 data), Google. sustainability.google/reports/
- Total water consumption, all operations, million gallons: 2020: 3,749; 2021: 4,562; 2022: 5,565; 2023: 6,352; 2024: 8,135. Appendix data tables, 2025 report. The 2026 report appendix continues the series: 2025: 10,869.
- 2024 detail: total withdrawal 11,011 million gallons; total discharge 2,876; data centers only: withdrawal 9,866, discharge 2,079, consumption 7,787; offices consumption 348. Appendix tables, 2025 report.
- 2025 detail: data centers only: withdrawal 13,562, discharge 3,039, consumption 10,523 million gallons. Appendix tables, 2026 report.
- Fleet-wide average PUE 2025: 1.09. 2026 report, energy section.
- Site table (2025 report) gives per-site withdrawal, discharge, and consumption in million gallons for data center campuses with use above 5 million gallons per year, broken out by water source (fresh municipal, fresh surface, groundwater, recycled, seawater). Example used in working notes: The Dalles, OR, 2024: withdrawal 461.1, consumption 361.4 million gallons.
- Classification: bucket 1 (company-disclosed, stated boundary: global, all operations unless the table says data centers only).

## S3. Microsoft Environmental Sustainability Report 2025 (fiscal 2024)

- Document: "2025 Environmental Sustainability Report", Microsoft, covering FY24 (year ending June 30, 2024). aka.ms/SustainabilityReport2025
- Total water consumed / withdrawn, all operations, cubic meters, chart "Total water consumption and withdrawal", Water section, p. 38: FY20: 4,196,000 / 4,773,000; FY21: 6,399,000 / 7,936,000; FY22: 8,068,000 / 10,706,000; FY23: 7,844,000 / 10,377,000; FY24: 5,807,000 / 12,951,000.
- Method caveat printed under the same chart: starting in FY24, reported values use an updated approach based on water use efficiency metrics for datacenter locations where actuals are not available; prior years were not adjusted to reflect the change. This is why the brief flags the FY24 consumption drop as partly a method change.
- Datacenter water usage effectiveness, withdrawal basis: 0.30 L/kWh in FY24, stated as a 39% improvement vs. 0.49 L/kWh in 2021. Water section.
- New cooling design: the report describes a datacenter design that consumes zero water for cooling, using chip-level cooling without evaporation, saving over 125,000 cubic meters of water annually per datacenter, based on the FY24 global average withdrawal WUE. Water section and overview letter.
- Classification: bucket 1 (company-disclosed, global, all operations; FY24 partly estimated under the stated new method).

## S4. Meta 2025 Environmental Data Index (calendar 2024)

- Document: "2025 Environmental Data Index", Meta, data for fiscal/calendar 2024, Sections 3.1-3.2. sustainability.atmeta.com/asset/2025-esg-data-index/
- Total water withdrawal, megaliters: 2020: 3,726; 2021: 5,043; 2022: 4,893; 2023: 5,274; 2024: 5,637. Of the 2024 total, data centers 4,145 and offices 1,492. An additional 1,019 megaliters withdrawn for data center construction in 2024 is explicitly excluded.
- Total water consumption, megaliters: 2020: 2,202; 2021: 2,569; 2022: 2,638; 2023: 3,078; 2024: 3,123. Data centers total 2024: 2,974.
- Water use embedded in purchased electricity (indirect), megaliters, companywide: 2021: 31,924; 2022: 41,172; 2023: 55,475; 2024: 72,207. Net of contracted renewables, avoided consumption 2024: 67,132.
- Data center water usage effectiveness, L/kWh: 2020: 0.30; 2021: 0.26; 2022: 0.20; 2023: 0.18; 2024: 0.19.
- Water withdrawal from areas with high or extremely high baseline water stress, 2024: 1,704 megaliters. Recycled water 2024: 515 megaliters.
- Classification: bucket 1 (company-disclosed, global). Meta is the only hyperscaler in this set that publishes an indirect (electricity) water figure.

## S5. Amazon, first absolute disclosure (June 2026)

- Document: "How Amazon is making its data centers more water-efficient", About Amazon (Amazon's own news site), June 2026. aboutamazon.com/news/sustainability/amazon-data-center-water-usage
- 2025 global data center WUE: 0.12 L/kWh, stated as a 52% improvement in water efficiency since 2021.
- 2025 withdrawal: in 2025 Amazon withdrew about 2.5 billion gallons across its entire global data center footprint. Amazon's verb is "withdrew"; the brief does not restate it as consumption.
- Water positive progress: about 75% of the way to the 2030 water-positive goal; 2025 replenishment returned 3 gallons for every 4 used. Withdrawal at owned-and-operated sites decreased 2% from 2024 to 2025. Amazon states the 2025 replenishment and withdrawal data were assured by a third-party provider.
- Before June 2026, AWS published WUE and the water-positive commitment but no absolute total. That asymmetry is documented by the absence in prior sustainability reporting and by the June 2026 piece presenting the absolute figure for the first time.
- Classification: bucket 1 (company-disclosed, global, data centers only, withdrawal).

## S6. USGS, Estimated Use of Water in the United States in 2015

- Document: "Estimated Use of Water in the United States in 2015", US Geological Survey, Circular 1441 (Dieter et al.), June 2018, and its summary page. usgs.gov/publications/estimated-use-water-united-states-2015
- Total withdrawals 2015: 322 billion gallons per day, 9% less than 2010 and the lowest since before 1970.
- Thermoelectric power withdrawals: 133 Bgal/d, 41% of total. Irrigation withdrawals: 118 Bgal/d, 37% of total (42% of freshwater withdrawals). Public supply: 39 Bgal/d, 12%.
- Consumptive use, reported in 2015 for the first time since 1995 for these categories: irrigation 73.2 Bgal/d (62% of irrigation withdrawals); thermoelectric power 4.31 Bgal/d (3% of thermoelectric withdrawals).
- Why 2015 and not a newer year: later USGS compilations do not publish a comparable national consumptive-use split; 2015 is the most recent USGS compilation reporting consumption for irrigation and thermoelectric power. The brief labels every USGS figure as 2015.
- Classification: bucket 1/2 (federal compilation of reported and estimated use).

## Derived comparisons used in chart (c) and the text (all arithmetic shown)

- Data center direct consumption 2023 (S1): 66 billion liters = 17.4 billion gallons per year = about 47.8 million gallons per day.
- Share of USGS total withdrawals (S6): 17.4 billion gallons per year / (322 Bgal/d x 365) = 0.0148%, stated in the brief as about 0.015%. This compares a consumption figure with a withdrawal total; it is used only as an order-of-magnitude scale check and is labeled wherever it appears.
- Data center total consumption 2023 (S1): 66 + nearly 800 = about 866 billion liters = about 229 billion gallons per year = about 0.63 Bgal/d. Against USGS thermoelectric consumptive use of 4.31 Bgal/d (2015), that is about 15%.
- Hyperscaler disclosed 2024 consumption, three companies (S2, S3, S4): Google 8,135 million gallons (CY2024, global, all operations) + Microsoft 5,807,000 cubic meters = 1,534 million gallons (FY24, global, all operations) + Meta 3,123 megaliters = 825 million gallons (CY2024, global, all operations) = about 10.5 billion gallons. LBNL's US-only direct estimate for 2023 is 17.4 billion gallons. The comparison is shown in the brief with all three differences named: the company figures are global, cover all operations, and exclude colocation, enterprise, and every other operator.

## S7. Google, Measuring the Environmental Impact of AI Inference (August 2025)

- Document: "Measuring the environmental impact of AI inference at Google scale", Google, August 2025, arXiv:2508.15734.
- Median Gemini Apps text prompt, May 2025, comprehensive methodology: 0.24 Wh energy, 0.03 gCO2e, 0.26 mL water. The comprehensive method adds host CPU, idle capacity, and data center overhead to active accelerator energy.
- Narrow (pre-existing) methodology, same prompt population: 0.10 Wh, 0.12 mL water.
- Water definition: onsite consumption only. Water is computed from energy using a consumptive WUE (Category 2) of 1.15 L/kWh, the Google fleet average for 2023 and 2024. Water consumed generating electricity is excluded.
- The paper cites Altman's June 2025 figures (S7a) and the Ren et al. estimate (S8) as comparators, which is where the brief takes Altman's numbers from.
- S7a. Sam Altman, personal blog post, June 2025: an average ChatGPT query uses about 0.34 Wh and about 0.000085 gallons of water (0.32 mL converted). No methodology, sample, or boundary published. Classification: bucket 3 for method, bucket 1 for provenance (it is the operator's own stated average, unverifiable as published).
- Classification: bucket 1 (measured and disclosed by the operator, with published method), with the boundary limits stated above.

## S8. Ren et al., Making AI Less Thirsty (2023)

- Document: "Making AI Less Thirsty: Uncovering and Addressing the Secret Water Footprint of AI Models", Shaolei Ren et al., arXiv:2304.03271 (2023, revised).
- GPT-3 training in Microsoft's US data centers: 5.4 million liters total water consumption, including 700,000 liters of scope-1 onsite consumption. Abstract and Section 3.
- Inference: GPT-3 needs to consume a 500 mL bottle of water for roughly 10 to 50 question-and-answer interactions, varying by location and time; the paper's table implies about 10.5 to 70.4 requests per 500 mL across locations. Implied per-request water: 500/50 to 500/10 = 10 to 50 mL.
- Boundary: scope 1 plus scope 2 (onsite plus electricity generation), GPT-3-era model and infrastructure (2020-2023), US Microsoft data centers.
- Classification: bucket 2 (peer-circulated academic estimate with a stated method). The brief's bucket-3 exhibit is not this paper; it is the mutated version of this paper's figure (500 mL per prompt) that circulates without the per-10-to-50-requests denominator.

## S9. Epoch AI, How much energy does ChatGPT use? (February 2025)

- Document: Epoch AI, "How much energy does ChatGPT use?", Gradient Updates, February 2025. epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
- Estimate: a typical GPT-4o query uses approximately 0.3 Wh, from a bottom-up model of model architecture and response length. Energy only; no water figure published.
- Classification: bucket 2 (independent estimate with a stated method).

## S10. PJM, 2025/2026 Base Residual Auction results (July 2024)

- Document: PJM Interconnection, auction results announcement and report for the 2025/2026 RPM Base Residual Auction, July 30, 2024.
- Resource clearing price, RTO: $269.92 per MW-day, vs. $28.92 per MW-day in the 2024/2025 auction. Ratio: 9.3x (derived).
- PJM's own announcement attributed the increase to several causes together: decreased supply offers (generator retirements), increases in projected peak load, and FERC-approved market reforms. The brief prints this alongside the market monitor's attribution (S11) because the two are not the same claim.
- Follow-on facts used in Finding 5: the 2026/2027 auction (July 2025) cleared at the FERC-approved cap of $329.17 per MW-day across the footprint, per PJM's announcement as carried by trade press; on September 29, 2026, FERC accepted most elements of PJM's one-time reliability backstop procurement but suspended it (until February 28, 2027) over whether PJM had shown its proposed division of costs between existing customers and new large loads was just and reasonable, per Utility Dive's reporting of the order, October 2026.
- Classification: bucket 1 (market operator's published results).

## S11. PJM Independent Market Monitor, Part G analysis (June 2025)

- Document: "Analysis of the 2025/2026 RPM Base Residual Auction, Part G Revised", Monitoring Analytics, LLC (Independent Market Monitor for PJM), June 3, 2025. monitoringanalytics.com
- Actual 2025/2026 BRA revenues (Scenario 0): $14,687,047,358. Conclusions and Table, pp. 1-2 and appendix tables.
- Scenario 87 (existing data center load kept; forecast new data center load plus forecast growth of existing load, 4,654 MW, removed): revenues would have been $6,944,087,201. Forecast load therefore accounts for $7,742,960,157, an increase of 111.5% over the scenario without it.
- Scenario 88 (all data center load removed, 7,927 MW, embedded plus above-embedded): revenues would have been $5,354,943,499. Data center load, existing plus forecast, therefore accounts for $9,332,103,858 of the actual revenues: 63.5% of the actual total, and revenues 174.3% higher than the no-data-center scenario.
- Derived split: of the $9,332,103,858 data center increment, $7,742,960,157 (about 83%) is attributable to forecast load and $1,589,143,702 to existing load.
- The MMU's stated conclusion, paraphrased: data center load growth, actual and forecast, is the primary reason for the tight supply-demand balance and the high prices in the 2025/2026 auction, and the current conditions are almost entirely the result of large data center load additions rather than organic load growth.
- Classification: bucket 2 (counterfactual model by the market's independent monitor; a model, not a meter reading).

## S12. EU data center reporting regime

- Instruments: Directive (EU) 2023/1791 (recast Energy Efficiency Directive), Article 12, and Commission Delegated Regulation (EU) 2024/1364 establishing the common reporting scheme and database.
- Scope: data centers with installed IT power demand of 500 kW or more.
- Required reporting, annually to the EU database: total energy consumption, power usage effectiveness, water usage effectiveness, total water input, renewable energy share, waste heat reused, plus facility identification data. First reporting cycle ran in 2024 (reporting period May to September 2024, deadline September 2024), then annually.
- First-cycle coverage: the European Commission's assessment of the first reporting cycle found about 770 sites reporting, roughly 36% of the facilities estimated to be in scope; six member states submitted no reports. As reported in Commission summaries carried by Corporate Disclosures and trade press, September 2026.
- A delegated act proposing an A-to-G energy and water label built on the reported data was advanced by the Commission in September 2026; the brief does not rely on it.
- US comparison: no equivalent US federal reporting mandate for data center energy or water use was found as of October 12, 2026. US numbers in this brief exist because companies volunteer them and because Berkeley Lab models them.
- Classification: bucket 1 (law and regulator reporting).

## S13. The Dalles, Oregon (illustration, two sentences only)

- Google's data centers in The Dalles, Oregon consumed 274.5 million gallons of water in 2021. The figure came from city water records released in December 2022 after the City of The Dalles dropped a 13-month lawsuit against The Oregonian/OregonLive that had sought to keep the records confidential as a trade secret; Google confirmed the numbers would no longer be treated as a trade secret. Reporting: Associated Press and KNKX, December 2022; The Oregonian's reporter on the case was Mike Rogoway.
- Google's own later publication, "Data Center Water Profile: The Dalles" (April 2023), restates the 2021 figure as almost 275 million gallons.
- Google's 2025 Environmental Report site table (S2) reports The Dalles 2024 consumption at 361.4 million gallons, so the site is now inside Google's routine disclosure.

## Follow-up check on the December 2024 LBNL report (October 12, 2026) - resolved, brief revised

Before publication, a check was run for a reported follow-up LBNL data center energy assessment (covered by E&E News around June 2026) that might revise the December 2024 report (S1). A first pass on October 12, 2026 failed to locate it and recorded it as unconfirmed; that record was wrong. On re-check the same day, the follow-up was found and obtained in full from eScholarship: "United States Data Center Energy Usage Report: 2025 Update", LBNL-2001758, June 2026, entered above as S14. The brief was revised against the primary text on October 12, 2026: the electricity history now includes the update's 2024 estimate (192 TWh, 4.7%), S1's 2028 range is marked superseded, and the forward look is the update's 2030 Reference Case (649 TWh) and Compounded Uncertainty range (521 to 843 TWh). The update contains no water-use estimates, so no water figure changed; every water figure remains S1's (December 2024). Chart (a) was regenerated from the revised figures in code/charts.py; data/stats.json carries the new figures under the key lbnl_energy_2025_update.

## Dropped during verification (not used anywhere in the brief)

- Any "data centers use X% of the world's water" figure: no primary source states a defensible global share; versions in circulation trace to advocacy posts, not measurements.
- The Ceres "Water Behind the Watts" estimate (3.4 trillion gallons of freshwater for electricity generation in seven states, 2024): a modeled advocacy estimate published August 2026. It may be reasonable, but it is a model built on modeled inputs, and the brief's indirect-water story is already carried by LBNL (S1) and Meta's disclosure (S4). Excluded to keep the estimate stack one layer deep.
- "The Dalles used a quarter of the city's water": printed by The Register from The Oregonian's reporting; plausible, but the denominator (total city water use) was not verified to a primary document here, so the brief uses only the 274.5 million gallon figure itself.
- Per-query estimates for specific long or agentic prompts (for example, university estimates of 18 Wh-class queries): real research, but they answer a different question than the median-prompt dispute and would blur the method comparison.
- Microsoft FY25 figures circulating in secondary coverage (WUE 0.27 L/kWh; replenishment 14.2 million cubic meters): the 2026 Environmental Sustainability Report exists (published mid-2026), but its water data tables were not extracted and verified for this brief; the brief uses the fully verified 2025 report (FY24) and flags the edition used at every mention.
