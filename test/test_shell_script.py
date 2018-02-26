from tempfile import NamedTemporaryFile

from vaxrank.cli import main as run_shell_script

from .testing_helpers import data_path

cli_args_for_b16_seqdata = [
    "--vcf", data_path("b16.f10/b16.vcf"),
    "--bam", data_path("b16.f10/b16.combined.bam"),
    "--vaccine-peptide-length", "25",
    "--mhc-predictor", "random",
    "--mhc-alleles", "H2-Kb,H2-Db",
    "--padding-around-mutation", "5",
    "--include-mismatches-after-variant"
]

cli_args_for_b16_seqdata_real_predictor = [
    "--vcf", data_path("b16.f10/b16.vcf"),
    "--bam", data_path("b16.f10/b16.combined.bam"),
    "--vaccine-peptide-length", "25",
    "--mhc-predictor", "mhcflurry",
    "--mhc-alleles", "H2-Kb,H2-Db",
    "--mhc-epitope-lengths", "8",
    "--padding-around-mutation", "5",
    "--include-mismatches-after-variant"
]

def test_ascii_report():
    with NamedTemporaryFile(mode="r", delete=False) as f:
        ascii_args = cli_args_for_b16_seqdata + ["--output-ascii-report", f.name]
        run_shell_script(ascii_args)
        contents = f.read()
        lines = contents.split("\n")
        assert len(lines) > 0

def test_ascii_report_real_netmhc_predictor():
    with NamedTemporaryFile(mode="r", delete=False) as f:
        ascii_args = cli_args_for_b16_seqdata_real_predictor + [
            "--output-ascii-report", f.name]
        run_shell_script(ascii_args)
        contents = f.read()
        lines = contents.split("\n")
        assert len(lines) > 0
        no_variants_text = 'No variants'
        assert no_variants_text not in contents
