"""Text for the SD Importer pages, in every language. Built by tools/build_sdimporter.py.

Keep the privacy policy in step with the app (photo_manager_project), and update
EFFECTIVE_DATE when it changes.
"""

# code: (html lang, language name, text direction, app name)
LANGUAGES = {
    "en": ("en", "English", "ltr", "SD Importer"),
    "ja": ("ja", "日本語", "ltr", "SD Importer"),
    "ko": ("ko", "한국어", "ltr", "SD Importer"),
    "zh-hans": ("zh-Hans", "简体中文", "ltr", "SD Importer"),
    "zh-hant": ("zh-Hant", "繁體中文", "ltr", "SD Importer"),
}

EFFECTIVE_DATE = {
    "en": "October 10, 2026",
    "ja": "2026年10月10日",
    "ko": "2026년 10월 10일",
    "zh-hans": "2026年10月10日",
    "zh-hant": "2026年10月10日",
}

T = {
    "en": {
        "language": "Language",
        "support": "Support",
        "privacy": "Privacy Policy",
        "effective": "Effective date",
        "tagline": "Sort SD card photos into folders by capture date — safely.",
        "intro": [
            "SD Importer copies photos and videos from your camera's SD card into folders by capture date. "
            "Every copy is verified byte by byte, and nothing on your card is deleted unless you choose to.",
            "It is free. If you like it, you can leave a tip to support development.",
        ],
        "features": [
            "Sorts by the capture date (EXIF) of photos and the creation date of videos",
            "Custom folder names such as yyyy/yyyy-MM-dd",
            "Verified copies, automatic skipping of files already imported, resume after interruption",
            "Duplicate check with side-by-side comparison",
            "Progress in the menu bar, notifications, and history",
            "RAW, HEIC, and video support",
        ],
        "download": "Download",
        "github_release": "Download from GitHub",
        "faq_title": "Frequently asked questions",
        "faq": [
            ("My SD card does not appear in the list.",
             "Make sure the card is mounted in Finder, then press the refresh button next to the source. "
             "You can also choose any folder with “Folder…”."),
            ("The app asks me to allow access to the SD card.",
             "The Mac App Store version runs in a sandbox and can only read places you choose. "
             "Click “Allow Access…” and then “Allow” once; the same card will not ask again."),
            ("A photo was sorted into the wrong date folder.",
             "The app uses the capture date recorded in the photo. If a file has no such date, it uses the file’s creation date. "
             "Check the camera’s clock setting."),
            ("The copy stopped partway.",
             "Files that finished copying are kept. Press Start again and the app continues with the rest."),
            ("Can I restore source files after deleting them?",
             "No. Deleting from the source cannot be undone, so the app verifies that every copy is identical before deleting. "
             "Files moved to the Trash from the duplicate check can be restored from the Trash."),
        ],
        "contact": "Contact",
        "contact_note": "Questions and bug reports are welcome on GitHub.",
        "contact_button": "Open GitHub Issues",
        "privacy_sections": [
            ("Summary", [
                "SD Importer does not collect, send, or share any personal information. "
                "Your photos, videos, and history stay on your Mac.",
            ]),
            ("Information the app does not collect", [
                "The app has no accounts, analytics, advertising, or tracking. It does not send your files, file names, "
                "or usage data to the developer or to anyone else.",
            ]),
            ("Data stored on your Mac", [
                "Settings: the destination folder, the folder name format, and the places you allowed the app to access.",
                "History: the date, source and destination, the number of files, and the number of files per extension for each import "
                "and duplicate check. File names are not recorded.",
                "This data is stored only on your Mac. You can delete the history at any time with “Clear History…”, "
                "or remove everything by deleting the app.",
            ]),
            ("Access to your files", [
                "The app reads files only in the SD cards and folders you select, to copy them, verify copies, and check for duplicates. "
                "It writes only to the destination you choose. Files are deleted or moved to the Trash only when you choose to.",
            ]),
            ("Notifications", [
                "Completion notifications are shown on your Mac only.",
            ]),
            ("Tips (in-app purchases)", [
                "Tips in the Mac App Store version are processed by Apple. The developer does not receive your payment information. "
                "The GitHub version links to GitHub Sponsors, which is covered by GitHub’s privacy policy.",
            ]),
            ("Children", [
                "The app does not collect information from anyone, including children.",
            ]),
            ("Changes to this policy", [
                "If this policy changes, this page will be updated along with the effective date.",
            ]),
            ("Contact", [
                "For questions about this policy, please contact us through GitHub Issues.",
            ]),
        ],
    },
    "ja": {
        "language": "言語",
        "support": "サポート",
        "privacy": "プライバシーポリシー",
        "effective": "施行日",
        "tagline": "SDカードの写真を、撮影日ごとのフォルダに安全に整理。",
        "intro": [
            "SD Importer は、カメラのSDカードの写真と動画を、撮影日ごとのフォルダにコピーするアプリです。"
            "コピーしたファイルは1バイトずつ照合し、SDカードのファイルは自分で選ばない限り消えません。",
            "無料でお使いいただけます。気に入っていただけたら、チップで開発を応援していただけるとうれしいです。",
        ],
        "features": [
            "写真の撮影日時（EXIF）・動画の作成日時で振り分け",
            "フォルダ名は yyyy/yyyy-MM-dd や yyyy年MM月dd日 など自由に",
            "中身まで照合するコピー、取り込み済みの自動スキップ、途中からの再開",
            "重複ファイルのチェックと、並べての比較",
            "メニューバーの進捗表示・完了通知・履歴",
            "RAW・HEIC・動画に対応",
        ],
        "download": "ダウンロード",
        "github_release": "GitHub からダウンロード",
        "faq_title": "よくある質問",
        "faq": [
            ("SDカードが一覧に出てきません。",
             "Finder でカードが表示されているか確かめてから、コピー元の横の更新ボタンを押してください。"
             "「フォルダ…」から好きなフォルダを選ぶこともできます。"),
            ("SDカードへのアクセスの許可を求められます。",
             "Mac App Store 版はサンドボックスの中で動くため、選んだ場所しか読めません。"
             "「アクセスを許可…」を押して「許可」を一度選べば、同じカードでは次から聞かれません。"),
            ("写真が違う日付のフォルダに入りました。",
             "写真に記録された撮影日時を使います。撮影日時がないファイルは、ファイルの作成日を使います。"
             "カメラの時計の設定も確認してください。"),
            ("コピーが途中で止まりました。",
             "コピーが終わったファイルは残っています。もう一度「開始」を押すと、残りからコピーします。"),
            ("コピー元から削除したファイルは戻せますか？",
             "戻せません。そのため、削除する前に必ずコピー先と中身が同じかを照合します。"
             "重複チェックからゴミ箱に入れたファイルは、ゴミ箱から戻せます。"),
        ],
        "contact": "お問い合わせ",
        "contact_note": "ご質問や不具合の報告は GitHub で受け付けています。",
        "contact_button": "GitHub Issues を開く",
        "privacy_sections": [
            ("概要", [
                "SD Importer は、個人情報を収集・送信・共有しません。写真、動画、履歴は、お使いの Mac の中にだけ保存されます。",
            ]),
            ("収集しない情報", [
                "アカウント、利用状況の解析、広告、トラッキングは一切ありません。"
                "ファイル、ファイル名、利用状況を、開発者やほかの誰かに送ることはありません。",
            ]),
            ("Mac に保存するデータ", [
                "設定：コピー先のフォルダ、フォルダ名の形式、アクセスを許可した場所。",
                "履歴：取り込みと重複チェックごとの日時、コピー元とコピー先、件数、拡張子ごとの件数。ファイル名は記録しません。",
                "これらはお使いの Mac の中にだけ保存されます。履歴は「履歴を消去…」でいつでも消せます。アプリを削除すればすべて消えます。",
            ]),
            ("ファイルへのアクセス", [
                "選んだSDカードとフォルダの中のファイルを、コピー・照合・重複チェックのためにだけ読みます。"
                "書き込むのは選んだコピー先だけです。ファイルの削除やゴミ箱への移動は、あなたが選んだときだけ行います。",
            ]),
            ("通知", [
                "完了の通知は、お使いの Mac にだけ表示されます。",
            ]),
            ("チップ（アプリ内課金）", [
                "Mac App Store 版のチップの支払いは Apple が処理します。開発者が支払い情報を受け取ることはありません。"
                "GitHub 版のリンク先の GitHub Sponsors には、GitHub のプライバシーポリシーが適用されます。",
            ]),
            ("お子さまについて", [
                "このアプリは、お子さまを含め、どなたの情報も収集しません。",
            ]),
            ("このポリシーの変更", [
                "内容を変更する場合は、このページと施行日を更新してお知らせします。",
            ]),
            ("お問い合わせ", [
                "このポリシーについてのご質問は、GitHub Issues からお寄せください。",
            ]),
        ],
    },
    "ko": {
        "language": "언어",
        "support": "지원",
        "privacy": "개인정보 처리방침",
        "effective": "시행일",
        "tagline": "SD 카드 사진을 촬영일별 폴더로 안전하게 정리.",
        "intro": [
            "SD Importer는 카메라 SD 카드의 사진과 동영상을 촬영일별 폴더로 복사하는 앱입니다. "
            "복사한 파일은 한 바이트씩 대조하며, SD 카드의 파일은 직접 선택하지 않는 한 지워지지 않습니다.",
            "무료로 사용할 수 있습니다. 마음에 드셨다면 팁으로 개발을 응원해 주세요.",
        ],
        "features": [
            "사진의 촬영 일시(EXIF)와 동영상의 생성 일시로 분류",
            "yyyy/yyyy-MM-dd 등 자유로운 폴더 이름",
            "내용까지 대조하는 복사, 이미 가져온 파일 자동 건너뛰기, 중단 후 이어서 복사",
            "중복 파일 검사와 나란히 비교",
            "메뉴 막대 진행 표시, 완료 알림, 기록",
            "RAW, HEIC, 동영상 지원",
        ],
        "download": "다운로드",
        "github_release": "GitHub에서 다운로드",
        "faq_title": "자주 묻는 질문",
        "faq": [
            ("SD 카드가 목록에 나타나지 않습니다.",
             "Finder에서 카드가 보이는지 확인한 후 원본 옆의 새로 고침 버튼을 누르세요. '폴더…'에서 원하는 폴더를 선택할 수도 있습니다."),
            ("SD 카드 접근 허용을 요청합니다.",
             "Mac App Store 버전은 샌드박스에서 실행되므로 선택한 위치만 읽을 수 있습니다. "
             "'접근 허용…'을 누르고 '허용'을 한 번 선택하면 같은 카드는 다음부터 묻지 않습니다."),
            ("사진이 다른 날짜 폴더에 들어갔습니다.",
             "사진에 기록된 촬영 일시를 사용합니다. 촬영 일시가 없는 파일은 파일 생성일을 사용합니다. 카메라의 시계 설정도 확인하세요."),
            ("복사가 도중에 멈췄습니다.",
             "복사가 끝난 파일은 남아 있습니다. 다시 '시작'을 누르면 나머지부터 복사합니다."),
            ("원본에서 삭제한 파일을 되돌릴 수 있나요?",
             "되돌릴 수 없습니다. 그래서 삭제하기 전에 반드시 복사본과 내용이 같은지 대조합니다. "
             "중복 검사에서 휴지통으로 옮긴 파일은 휴지통에서 복원할 수 있습니다."),
        ],
        "contact": "문의",
        "contact_note": "질문과 버그 신고는 GitHub에서 받고 있습니다.",
        "contact_button": "GitHub Issues 열기",
        "privacy_sections": [
            ("요약", [
                "SD Importer는 개인정보를 수집, 전송, 공유하지 않습니다. 사진, 동영상, 기록은 사용자의 Mac에만 저장됩니다.",
            ]),
            ("수집하지 않는 정보", [
                "계정, 사용 분석, 광고, 추적이 전혀 없습니다. 파일, 파일 이름, 사용 정보를 개발자나 다른 누구에게도 보내지 않습니다.",
            ]),
            ("Mac에 저장하는 데이터", [
                "설정: 저장 위치 폴더, 폴더 이름 형식, 접근을 허용한 위치.",
                "기록: 가져오기와 중복 검사마다의 날짜, 원본과 저장 위치, 파일 수, 확장자별 파일 수. 파일 이름은 기록하지 않습니다.",
                "이 데이터는 사용자의 Mac에만 저장됩니다. 기록은 '기록 지우기…'로 언제든지 지울 수 있으며, 앱을 삭제하면 모두 지워집니다.",
            ]),
            ("파일 접근", [
                "선택한 SD 카드와 폴더 안의 파일을 복사, 대조, 중복 검사를 위해서만 읽습니다. "
                "쓰기는 선택한 저장 위치에만 합니다. 파일 삭제나 휴지통 이동은 사용자가 선택했을 때만 합니다.",
            ]),
            ("알림", ["완료 알림은 사용자의 Mac에만 표시됩니다."]),
            ("팁(앱 내 구입)", [
                "Mac App Store 버전의 팁 결제는 Apple이 처리합니다. 개발자는 결제 정보를 받지 않습니다. "
                "GitHub 버전에서 연결되는 GitHub Sponsors에는 GitHub의 개인정보 처리방침이 적용됩니다.",
            ]),
            ("아동", ["이 앱은 아동을 포함한 누구의 정보도 수집하지 않습니다."]),
            ("방침 변경", ["내용이 변경되면 이 페이지와 시행일을 업데이트하여 알려 드립니다."]),
            ("문의", ["이 방침에 대한 질문은 GitHub Issues로 보내 주세요."]),
        ],
    },
    "zh-hans": {
        "language": "语言",
        "support": "支持",
        "privacy": "隐私政策",
        "effective": "生效日期",
        "tagline": "按拍摄日期，把 SD 卡照片安全地整理到文件夹。",
        "intro": [
            "SD Importer 可将相机 SD 卡中的照片和视频按拍摄日期复制到文件夹中。"
            "复制的文件会逐字节核对，除非您选择删除，SD 卡上的文件不会被删除。",
            "可免费使用。如果喜欢，欢迎用小费支持开发。",
        ],
        "features": [
            "按照片的拍摄时间（EXIF）和视频的创建时间整理",
            "可自由设置文件夹名称，如 yyyy/yyyy-MM-dd",
            "逐字节核对的复制、自动跳过已导入的文件、中断后继续",
            "重复文件检查与并排比较",
            "菜单栏进度、完成通知和历史记录",
            "支持 RAW、HEIC 和视频",
        ],
        "download": "下载",
        "github_release": "从 GitHub 下载",
        "faq_title": "常见问题",
        "faq": [
            ("列表中没有显示 SD 卡。",
             "请确认访达中能看到该卡，然后按来源旁边的刷新按钮。也可以通过“文件夹…”选择任意文件夹。"),
            ("应用要求允许访问 SD 卡。",
             "Mac App Store 版本在沙盒中运行，只能读取您选择的位置。点按“允许访问…”并选择一次“允许”后，同一张卡以后不会再询问。"),
            ("照片被放进了错误日期的文件夹。",
             "应用使用照片中记录的拍摄时间。没有拍摄时间的文件会使用文件的创建日期。也请检查相机的时钟设置。"),
            ("复制中途停止了。",
             "已复制完成的文件会保留。再次按“开始”即可从剩余部分继续复制。"),
            ("从来源删除的文件可以恢复吗？",
             "无法恢复。因此在删除之前，应用一定会核对副本内容是否相同。在重复检查中移到废纸篓的文件可以从废纸篓恢复。"),
        ],
        "contact": "联系我们",
        "contact_note": "欢迎在 GitHub 上提问或报告问题。",
        "contact_button": "打开 GitHub Issues",
        "privacy_sections": [
            ("概要", ["SD Importer 不收集、发送或共享任何个人信息。照片、视频和历史记录只保存在您的 Mac 上。"]),
            ("不收集的信息", ["没有账户、使用分析、广告或跟踪。不会将您的文件、文件名或使用数据发送给开发者或任何人。"]),
            ("保存在 Mac 上的数据", [
                "设置：目标文件夹、文件夹名称格式，以及您允许访问的位置。",
                "历史记录：每次导入和重复检查的日期、来源和目标位置、文件数量以及各扩展名的文件数量。不记录文件名。",
                "这些数据只保存在您的 Mac 上。可随时通过“清除历史…”删除历史记录，删除应用即可清除全部数据。",
            ]),
            ("文件访问", [
                "仅为复制、核对和检查重复而读取您所选 SD 卡和文件夹中的文件。只写入您选择的目标位置。只有在您选择时才会删除文件或移到废纸篓。",
            ]),
            ("通知", ["完成通知只显示在您的 Mac 上。"]),
            ("小费（App 内购买）", [
                "Mac App Store 版本的小费付款由 Apple 处理，开发者不会收到您的付款信息。GitHub 版本链接的 GitHub Sponsors 适用 GitHub 的隐私政策。",
            ]),
            ("儿童", ["本应用不收集任何人的信息，包括儿童。"]),
            ("政策变更", ["如有变更，将更新本页面及生效日期。"]),
            ("联系我们", ["如对本政策有疑问，请通过 GitHub Issues 联系我们。"]),
        ],
    },
    "zh-hant": {
        "language": "語言",
        "support": "支援",
        "privacy": "隱私權政策",
        "effective": "生效日期",
        "tagline": "依拍攝日期，把 SD 卡照片安全地整理到資料夾。",
        "intro": [
            "SD Importer 可將相機 SD 卡中的照片和影片依拍攝日期複製到資料夾中。"
            "複製的檔案會逐位元組核對，除非您選擇刪除，SD 卡上的檔案不會被刪除。",
            "可免費使用。如果喜歡，歡迎用小費支持開發。",
        ],
        "features": [
            "依照片的拍攝時間（EXIF）和影片的建立時間整理",
            "可自由設定資料夾名稱，如 yyyy/yyyy-MM-dd",
            "逐位元組核對的複製、自動略過已匯入的檔案、中斷後繼續",
            "重複檔案檢查與並排比較",
            "選單列進度、完成通知和歷史記錄",
            "支援 RAW、HEIC 和影片",
        ],
        "download": "下載",
        "github_release": "從 GitHub 下載",
        "faq_title": "常見問題",
        "faq": [
            ("列表中沒有顯示 SD 卡。",
             "請確認 Finder 中能看到該卡，然後按來源旁邊的重新整理按鈕。也可以透過「資料夾…」選擇任意資料夾。"),
            ("App 要求允許存取 SD 卡。",
             "Mac App Store 版本在沙盒中執行，只能讀取您選擇的位置。按「允許存取…」並選擇一次「允許」後，同一張卡之後不會再詢問。"),
            ("照片被放進了錯誤日期的資料夾。",
             "App 使用照片中記錄的拍攝時間。沒有拍攝時間的檔案會使用檔案的建立日期。也請檢查相機的時鐘設定。"),
            ("複製中途停止了。",
             "已複製完成的檔案會保留。再次按「開始」即可從剩餘部分繼續複製。"),
            ("從來源刪除的檔案可以復原嗎？",
             "無法復原。因此在刪除之前，App 一定會核對副本內容是否相同。在重複檢查中移到垃圾桶的檔案可以從垃圾桶復原。"),
        ],
        "contact": "聯絡我們",
        "contact_note": "歡迎在 GitHub 上提問或回報問題。",
        "contact_button": "開啟 GitHub Issues",
        "privacy_sections": [
            ("概要", ["SD Importer 不收集、傳送或分享任何個人資料。照片、影片和歷史記錄只儲存在您的 Mac 上。"]),
            ("不收集的資料", ["沒有帳號、使用分析、廣告或追蹤。不會將您的檔案、檔案名稱或使用資料傳送給開發者或任何人。"]),
            ("儲存在 Mac 上的資料", [
                "設定：目標資料夾、資料夾名稱格式，以及您允許存取的位置。",
                "歷史記錄：每次匯入和重複檢查的日期、來源和目標位置、檔案數量以及各副檔名的檔案數量。不記錄檔案名稱。",
                "這些資料只儲存在您的 Mac 上。可隨時透過「清除歷史…」刪除歷史記錄，刪除 App 即可清除全部資料。",
            ]),
            ("檔案存取", [
                "僅為複製、核對和檢查重複而讀取您所選 SD 卡和資料夾中的檔案。只寫入您選擇的目標位置。只有在您選擇時才會刪除檔案或移到垃圾桶。",
            ]),
            ("通知", ["完成通知只顯示在您的 Mac 上。"]),
            ("小費（App 內購買）", [
                "Mac App Store 版本的小費付款由 Apple 處理，開發者不會收到您的付款資訊。GitHub 版本連結的 GitHub Sponsors 適用 GitHub 的隱私權政策。",
            ]),
            ("兒童", ["本 App 不收集任何人的資料，包括兒童。"]),
            ("政策變更", ["如有變更，將更新本頁面及生效日期。"]),
            ("聯絡我們", ["如對本政策有疑問，請透過 GitHub Issues 聯絡我們。"]),
        ],
    },
}
