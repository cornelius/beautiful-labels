from labels import Labels

def test_save(tmp_path):
    labels = Labels("someorg", "somerepo")
    labels.add_label("scanned", 1166740325, "another label", "", "EE7912")
    labels.add_label("scanned", 1097075204, "bug", "Something isn't working", "d73a4a")
    labels.add_label("scanned", 1167038964, "common issue", "Label used across repositories", "333333")

    actual_file = tmp_path / 'labels.yaml'
    labels.save(str(actual_file))
    with open('test_data/labels.yaml') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()
