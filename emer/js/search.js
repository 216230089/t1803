$(function() {
    // 초기화 설정
    EmergencyRoomGeneral.init();

    // 상세페이지로 이동
    $('body').on('click', '.move-detail-page', function(event) {
        event.preventDefault();

        EmergencyRoomGeneral.moveDetailPage($(this).data('key'));
    });

    // 검색 버튼 선택
    $('body').on('submit', '#frmGeneralSearch', function() {
        return EmergencyRoomGeneral.retrieveData();
    });

    // 엑셀 다운로드
    $('body').on('click', '#excelDownloadButton', EmergencyRoomGeneral.excelDownload);
});

/**
 * (일반)응급실 찾기
 * @type {{init: *}}
 */
var EmergencyRoomGeneral = {
    _searchCondition : null,
    /**
     * 초기화 설정
     */
    init : function() {
        // 좌표가 있을 경우 좌표정보를 주소로 변환
        if(navigator.geolocation) { // HTML5 GeoLocation 기능을 이용해서 사용자 접속 위치 좌표 추출
            navigator.geolocation.getCurrentPosition(function(position) {
                $('#hiddenLatitude').val(position.coords.latitude);		// 위도
                $('#hiddenLongitude').val(position.coords.longitude);	// 경도
                $('input[name="lat"]').val(position.coords.latitude);	// 검색조건에 사용되는 위도
                $('input[name="lon"]').val(position.coords.longitude);	// 검색조건에 사용되는 경도

                // 좌표가 있을 경우 좌표정보를 주소로 변환
                var coords = new daum.maps.LatLng($('#hiddenLatitude').val(), $('#hiddenLongitude').val());
                MapUtil.getAddrInfoByCoordinates(coords, $('#hiddenAddress'));
            },
            function(error) {
                switch(error.code){
                    case error.PERMISSION_DENIED :
                        // 사용자가 위치정보에 대한 요청을 거부
                        console.log('User denied the request for Geolocation.');
                        break;
                    case error.POSITION_UNAVAILABLE :
                        // 위치정보 사용이 불가능할 때(주로 PC)
                        console.log('Location information is unavailable.');
                        break;
                    case error.TIMEOUT :
                        // 시간초과
                        console.log('The request to get user location timed out.');
                        break;
                    case error.UNKNOWN_ERROR :
                        // 알 수 없는 에러
                        console.log('An unknown error occurred.');
                        break;
                }
            });
        }
    },
    /**
     * 상세페이지 이동 함수
     * @param key 기관코드
     */
    moveDetailPage : function(key) {
        var paramData = {
            'emogcode' : key,
            'lat' : $('#hiddenLatitude').val(),
            'lon' : $('#hiddenLongitude').val(),
            'fromAddress' : $('#hiddenAddress').val(),
            'emogdesc' : $('#emogdesc').val(),
            'sidoCode' : $('[name="sidoCode"]').val(),
            'gugunCode' : $('[name="gugunCode"]').val(),
            'dongCode' : $('[name="dongCode"]').val(),
            'addrhosp' : $('[name="addrhosp"]').val(),
            'emogdstr' : $('[name="emogdstr"]').val(),
            'loca' : $('[name="loca"]').val(),
            'searchType' : $('[name="searchType"]').val(),
        };
        EmergencyRoomGeneral._searchCondition = paramData;

        var $detailForm = $('#detailForm');
        $detailForm.find('input[name="jsonSearchCondition"]').val(JSON.stringify(EmergencyRoomGeneral._searchCondition));
        $detailForm.submit();
    },
    /**
     * 응급실 찾기 목록 조회
     */
    retrieveData : function() {
        // 유효성 검사
        var $sidoCode = $('.general-sido');
        if($sidoCode.val() === '') {
            alert('시도를 선택해주세요.');
            return false;
        }

        // 로딩 이미지 생성
        JsUtil.showLoading();

        return true;
    },
    /**
     * 엑셀 다운로드
     */
    excelDownload : function() {
        var generalSidoCode = $('#generalSidoCode').val();
        var generalGugunCode = $('#generalGugunCode').val();
        var generalDongCode = $('#generalDongCode').val();
        var emogdesc = $('#emogdesc').val();
        var params = '?loca=' + generalSidoCode + '&emogdstr=' + generalGugunCode + '&addrhosp=' + generalDongCode + '&emogdesc=' + emogdesc;

        if(generalSidoCode === '') {
            alert('시도를 선택해주세요.');
            return false;
        }

        window.location.href='/egen/get_emergency_room_excel.do' + params;
        return false;
    } 
}