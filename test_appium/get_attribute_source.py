'''
public enum Attribute {
    CHECKABLE(new String[]{"checkable"}),
    CHECKED(new String[]{"checked"}),
    CLASS(new String[]{"class", "className"}),
    CLICKABLE(new String[]{"clickable"}),
    CONTENT_DESC(new String[]{"content-desc", "contentDescription"}),
    ENABLED(new String[]{"enabled"}),
    FOCUSABLE(new String[]{"focusable"}),
    FOCUSED(new String[]{"focused"}),
    LONG_CLICKABLE(new String[]{"long-clickable", "longClickable"}),
    PACKAGE(new String[]{"package"}),
    PASSWORD(new String[]{"password"}),
    RESOURCE_ID(new String[]{"resource-id", "resourceId"}),
    SCROLLABLE(new String[]{"scrollable"}),
    SELECTION_START(new String[]{"selection-start"}),
    SELECTION_END(new String[]{"selection-end"}),
    SELECTED(new String[]{"selected"}),
    TEXT(new String[]{"text", "name"}),
    // The main difference of this attribute from the preceding one is that
    // it does not replace null values with empty strings
    ORIGINAL_TEXT(new String[]{"original-text"}, false, false),
    BOUNDS(new String[]{"bounds"}),
    INDEX(new String[]{"index"}, false, true),
    DISPLAYED(new String[]{"displayed"}),
    CONTENT_SIZE(new String[]{"contentSize"}, true, false);
'''
