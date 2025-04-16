import re


def parse_foundry_sequence(sequence):
    test_code = "function testGenerated() public {\n"

    # Regex pattern to extract details from each line in the sequence
    pattern = re.compile(
        r"sender=(0x[0-9a-fA-F]+)"  # Matches sender address
        r".*?addr=\[.*?\](0x[0-9a-fA-F]+)"  # Matches contract address
        r".*?calldata=(\w+)\((.*?)\)"  # Matches function name and parameter types
        r".*?args=\[(.*?)\](?=\s*(?:\n|$))"  # Matches function arguments until end of line
    )

    for match in pattern.finditer(sequence):
        sender, contract, calldata, param_types, args = match.groups()

        # Split the args string but preserve numbers after commas
        cleaned_args = []
        current_arg = ""
        in_brackets = 0

        for char in args:
            if char == "[":
                in_brackets += 1
            elif char == "]":
                in_brackets -= 1
            elif char == "," and in_brackets == 0:
                # Add the current argument if it exists
                base_value = current_arg.split("[")[0].strip()
                if base_value:
                    cleaned_args.append(base_value)
                current_arg = ""
                continue
            current_arg += char

        # Don't forget the last argument
        if current_arg:
            base_value = current_arg.split("[")[0].strip()
            if base_value:
                cleaned_args.append(base_value)

        # Generate Solidity function call with vm.prank
        test_code += f"    {calldata}({', '.join(cleaned_args)});\n"

    test_code += "}"
    return test_code


# Test the function
sequence = """	
	  sender=0x0000000000000000000000000000000000000013 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[189122219882571799774772864941647259190304340115841899 [1.891e53], 6]
                sender=0x0000000000000000000000000000000000000013 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[13655457928693112409472053095577207897263864182804850092563982809652935417 [1.365e73], 0]
                sender=0x9B80cc26E9107B8dDCF3dfcddB8c63D314027Fac addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=depositToCollateralV3(int24,int24,uint128,uint256) args=[8388605 [8.388e6], 527978 [5.279e5], 10544469795529919267485545770 [1.054e28], 115792089237316195423570985008687907853269984665640564039457584007913129639934 [1.157e77]]
                sender=0x00000000000000000000000000000000000047e8 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=splitV3(uint256,uint256,uint256) args=[11557 [1.155e4], 3610, 4588]
                sender=0x00000000000000000000000000000000000003e8 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=joinV3(uint256) args=[731568215600161167850487632188642832288189798089467132 [7.315e53]]
                sender=0x691D3d9df2aFaE8Bb8710F7Fe1C783435abBce98 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[19832945266573261727763993627943676626754868608254892 [1.983e52], 0]
                sender=0x0000000000000000000000000000000000000710 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=liquidateV3(uint256,uint256,uint8,bool) args=[7968254273814597001097907689364077324114105 [7.968e42], 1642041987830816406270576901087007330343011415232635385 [1.642e54], 44, false]
                sender=0xe93B0048DeE68aD8Fa0A6121fFC4984fb31D7475 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=lendToV3Borrowable(uint256,uint8) args=[1, 121]
                sender=0x00000000000000000000000000000002540C29C7 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[156, 65]
                sender=0x0000000000000000000000000000000001F8c1c7 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=joinV3(uint256) args=[226140011452977417688103452283369714599547928181373890 [2.261e53]]
                sender=0x0000000000000000000000000000000000006006 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=lendToV3Borrowable(uint256,uint8) args=[258042483539500453725636032398644151045959915079578 [2.58e50], 8]
                sender=0x823f1c90c50556D7A3804dCDB1d44b2FBe43f65D addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=liquidateV3(uint256,uint256,uint8,bool) args=[115792089237316195423570985008687907853269984665640564039457584007913129639933 [1.157e77], 99366495637707233545795199728221858748686 [9.936e40], 16, true]
                sender=0x0000000000000000000000000000000000004899 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=borrowTokenV3(uint256,uint8) args=[66363293025249157958109056755820628238934684 [6.636e43], 15]
                sender=0x0000000000000000000000000000000000001785 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[10377189112183424601032150213981562159279150232482156911353266324930061 [1.037e70], 255]
                sender=0x0000000000000000000000000000000000005586 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=mintV3NFT(int24,int24,uint128,uint256) args=[-19006 [-1.9e4], -120, 455812608380 [4.558e11], 92078419247869482986488556954256787 [9.207e34]]
                sender=0x000000000000000000000000000000000000063c addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=restructureBadDebt(uint256,uint256,uint8) args=[12700416277808977 [1.27e16], 201782856496156562550590117764548857337193282428020279848527367 [2.017e62], 0]
                sender=0x0000000000000000000000000000000000000066 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=depositToCollateralV3(int24,int24,uint128,uint256) args=[203, 2, 347250691739400335767156910470 [3.472e29], 8929264722588166781 [8.929e18]]
                sender=0x0000000000000000000000000000000000000039 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[84378665959361287077 [8.437e19], 38]
                sender=0x00000000000000000000000000000000000023ef addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=doFeeGrowthV3(uint256,uint256,uint256) args=[3152, 23732 [2.373e4], 42588 [4.258e4]]
                sender=0x0000000000000000000000000000000000002810 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[192030660350685745148917486766292805801596491664731707625605413389730452962 [1.92e74], 0]
                sender=0x00000000000000000000000000000000000001fa addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=splitV3(uint256,uint256,uint256) args=[3381880346935781415267374833631377156582527 [3.381e42], 2503516433490069998544846723227503055782087174195187896746339405016526190416 [2.503e75], 1420868063942599858325135009945086322062877669184280370251105642973226 [1.42e69]]
                sender=0xe858283b16d8be62d2e76ade8ABC7F59833e1ce2 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=joinV3(uint256) args=[10213 [1.021e4]]
                sender=0x000000000000000000000000000000000000000E addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=liquidateV3(uint256,uint256,uint8,bool) args=[7576, 251802541008676516341833211319 [2.518e29], 0, false]
                sender=0x00000000000000000000001c81dBB8FE7167BfA5 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=doFeeGrowthV3(uint256,uint256,uint256) args=[2602, 15913 [1.591e4], 4595]
                sender=0x000000000000000000000000000000000000298d addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[638841728701 [6.388e11], 4]
                sender=0x000000000000000000000000000000013Eb6C9A6 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=reinvestPositionV3(uint256,int24,int24,uint256,uint256) args=[2451, -8367020 [-8.367e6], -8388608 [-8.388e6], 6988, 10020 [1.002e4]]
                sender=0x00000000000000000000000000000000000004f2 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[16814 [1.681e4], 31]
                sender=0x0000000000000000000000000000000000001097 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=liquidateV3(uint256,uint256,uint8,bool) args=[2646777771 [2.646e9], 16431 [1.643e4], 206, false]
                sender=0x04aceA83Ff3DeA964100d47587fc07D824ffCBba addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=depositToCollateralV3(int24,int24,uint128,uint256) args=[85974 [8.597e4], 96, 1106863701893141766085 [1.106e21], 5124981000385169112491841004953644987777623768777059590118 [5.124e57]]
                sender=0x5C2Cd4C92701b78Cb750445a1bF19758Fca7fD6b addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[23280701457367622263843623601737013821102244461348489650 [2.328e55], 169]
                sender=0x344eDe89ccCF22569DB39C46899a17C18a0Ee115 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[19338 [1.933e4], 41]
                sender=0x0000000000000000000000000000000000002889 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=redeemV3NFT(uint256) args=[2737]
                sender=0x0000000000000000000000000000000000002137 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=joinV3(uint256) args=[115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77]]
                sender=0x86a3e7BEBB58872A12e90Ffb75411B2F87C3b6E8 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=lendToV3Borrowable(uint256,uint8) args=[7484, 78]
                sender=0xcd86161f2D240f92E190691d131E02c090e7e749 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=redeemV3NFT(uint256) args=[5007834641080981446154381272022150904742 [5.007e39]]
                sender=0x0000000000000000000000000000000000005d8F addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=doFeeGrowthV3(uint256,uint256,uint256) args=[11592 [1.159e4], 4159, 13870 [1.387e4]]
                sender=0x0000000000000000000000000000000000000c30 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[344300470576801332017469669559997088514102920362288014979358326730022148 [3.443e71], 1]
                sender=0xfa984BC258Fd38d52f507fC502e5e4366408E8Ac addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[10090655059439302405201567319228881451732037736423092328927231093384193782611 [1.009e76], 0]
                sender=0x000000000000000114617c414E75673b86a9B286 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=depositToCollateralV3(int24,int24,uint128,uint256) args=[-8385735 [-8.385e6], -8384826 [-8.384e6], 2940, 5765]
                sender=0x0000000000000000000000000000000000003507 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=restructureBadDebt(uint256,uint256,uint8) args=[92697285658906 [9.269e13], 26, 53]
                sender=0x00000000000000000000000000000000000054F8 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=redeemV3NFT(uint256) args=[867]
                sender=0x0000000000000000000000000000000000005FA5 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[420938344556762094673127642 [4.209e26], 101]
                sender=0x0000000000000000000000000000000000000188 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=joinV3(uint256) args=[13741 [1.374e4]]
                sender=0x0000000000000000000000000000000000000Fbe addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=liquidateV3(uint256,uint256,uint8,bool) args=[1584179462183917634778664835 [1.584e27], 335772050093640259166955595744837051250204623660404668506 [3.357e56], 252, true]
                sender=0x49385BEb0C7f2DD11388c37Ec8Ab0E08c96a96C7 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=depositToCollateralV3(int24,int24,uint128,uint256) args=[14614 [1.461e4], 2, 424492738 [4.244e8], 13767677922944236045581168877425458812295 [1.376e40]]
                sender=0x0000000000000004f6aB9b3a89168929DEFB1370 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=joinV3(uint256) args=[15148 [1.514e4]]
                sender=0xdF98227cCa41409c9EcD1ac800768E93ACcE78af addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=mintV3NFT(int24,int24,uint128,uint256) args=[21, -123703 [-1.237e5], 68101316161819033 [6.81e16], 40750250289436890322900123081827460756755 [4.075e40]]
                sender=0x1be5d6E09EAFB8822F443A1b6266Ee5078D21A3E addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=doFeeGrowthV3(uint256,uint256,uint256) args=[3, 1263347535005522153424343206 [1.263e27], 445924592519834190229959461247351541407 [4.459e38]]
                sender=0x0000000000000000000000000000000000004D94 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[115792089237316195423570985008687907853269984665640564039457584007913129639934 [1.157e77], 58]
                sender=0x0000000000000000000000000000000000000095 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=joinV3(uint256) args=[342695861616940689952238323003275754327405343540214 [3.426e50]]
                sender=0x00000000000000000000b77183C5207965936F12 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=borrowTokenV3(uint256,uint8) args=[7984, 251]
                sender=0x0000000000000000000000000000000000008FE0 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[7922, 152]
                sender=0x33BEFaC5Dd7AaA54e1e70e7b2c15FF67e3794cdC addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[356160611545506189442803 [3.561e23], 136]
                sender=0x7f557a09162e42E5353d5a0d8C047A8f5F8d0315 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=lendToV3Borrowable(uint256,uint8) args=[1013114376017796158685253966 [1.013e27], 6]
                sender=0xea5756Eaa1178Fd3a7D541f830BB32C928DE6746 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=liquidateV3(uint256,uint256,uint8,bool) args=[24556 [2.455e4], 2262432369397662082577498687410349797515867446 [2.262e45], 178, true]
                sender=0x00000000000000000000000000000000000029eA addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=redeemV3NFT(uint256) args=[12883 [1.288e4]]
                sender=0x00000000000000000000000000000000000012d7 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=splitV3(uint256,uint256,uint256) args=[7089, 1906, 18070 [1.807e4]]
                sender=0x00000000000000000000000000000000000001F4 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=reinvestPositionV3(uint256,int24,int24,uint256,uint256) args=[5190, -8381940 [-8.381e6], -8372844 [-8.372e6], 923, 73201476287530688802521594523384887872805305497983380531069841047127901235290 [7.32e76]]
                sender=0x00000000000000013DAaE6cea245A24A77Bec4dc addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=borrowTokenV3(uint256,uint8) args=[9757, 51]
                sender=0x000000000000000000000000000000000000565a addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=depositToCollateralV3(int24,int24,uint128,uint256) args=[-50437 [-5.043e4], 5, 440145963290928431227003079 [4.401e26], 3]
                sender=0x000000000000000000000000000000000000128F addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=lendToV3Borrowable(uint256,uint8) args=[762, 113]
                sender=0x000000000000000000000000000000000000116b addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=reinvestPositionV3(uint256,int24,int24,uint256,uint256) args=[11164 [1.116e4], -8388607 [-8.388e6], -8374985 [-8.374e6], 14110 [1.411e4], 523]
                sender=0x0000000000000000000000019C6163e7387f316e addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=doFeeGrowthV3(uint256,uint256,uint256) args=[5414, 117122 [1.171e5], 5268494147677028751901585758298917952801060236650442916098 [5.268e57]]
                sender=0x0000000000000005FA00332E684D13d3559d4143 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=redeemV3NFT(uint256) args=[115792089237316195423570985008687907853269984665640564039457584007913129639933 [1.157e77]]
                sender=0x00000000000000000000D14D3f748ED2b2c36354 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=joinV3(uint256) args=[1735]
                sender=0xbe909e908b386B041C34BAE139afB449937C6c3A addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=mintV3NFT(int24,int24,uint128,uint256) args=[-8385741 [-8.385e6], -8383862 [-8.383e6], 77642486302155903151820282942362492967 [7.764e37], 3620]
                sender=0x0000000000000000000000000000000000005d8b addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=liquidateV3(uint256,uint256,uint8,bool) args=[3730, 123990586117447099827985809 [1.239e26], 11, false]
                sender=0x0000000000000000000000000000000000001b9D addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[86400 [8.64e4], 44]
                sender=0x00000000000000070d205Ee3e4EbCEE10e2a1AAB addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=repayTokenV3(uint256,uint8) args=[1192, 144]
                sender=0x0000000000000000000000000000000000005e58 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=depositToCollateralV3(int24,int24,uint128,uint256) args=[-1, 1, 2792, 1008942243 [1.008e9]]
                sender=0x0000000000000000000000000000000099fBab87 addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=redeemV3NFT(uint256) args=[115792089237316195423570985008687907853269984665640564039457584007913129639932 [1.157e77]]
                sender=0x0000000000000000000000000000000000005f2C addr=[test/fuzzing/FoundryPlayground.sol:FoundryPlayground]0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496 calldata=borrowTokenV3(uint256,uint8) args=[64612068923720054750411954145189777452804336814 [6.461e46], 111]
		"""

print(parse_foundry_sequence(sequence))
