<!-- source: https://ui.nuxt.com/components/locale-select --> # LocaleSelectPRO

[SelectMenu](/components/select-menu)[GitHub](https://github.com/nuxt/ui-
pro/blob/v3/src/runtime/components/locale/LocaleSelect.vue)

A Select to switch between locales.

## Usage

The LocaleSelect component extends the [SelectMenu](/components/select-menu)
component, so you can pass any property such as `color`, `variant`, `size`,
etc.

[](/getting-started/i18n/nuxt)This component is meant to be used with the
**i18n** system. Learn more about it in the guide.

[](/getting-started/i18n/vue)This component is meant to be used with the
**i18n** system. Learn more about it in the guide.

The flags are displayed using Unicode characters. This may result in a
different display, e.g. Microsoft Edge under Windows displays the ISO 3166-1
alpha-2 code instead, as no flag icons are shipped with the OS fonts.

### Locales

Use the `locales` prop with an array of locales from `@nuxt/ui/locale`.

🇬🇧English

    
    
    <script setup lang="ts">
    import * as locales from '@nuxt/ui/locale'
    
    const locale = ref('en')
    </script>
    
    <template>
      <ULocaleSelect v-model="locale" :locales="Object.values(locales)" class="w-48" />
    </template>
    

You can pass only the locales you need in your application:

    
    
    <script setup lang="ts">
    import { en, es, fr } from '@nuxt/ui/locale'
    
    const locale = ref('en')
    </script>
    
    <template>
      <ULocaleSelect v-model="locale" :locales="[en, es, fr]" />
    </template>
    

### Dynamic locale

You can use it with Nuxt i18n:

    
    
    <script setup lang="ts">
    import * as locales from '@nuxt/ui/locale'
    
    const { locale } = useI18n()
    </script>
    
    <template>
      <ULocaleSelect v-model="locale" :locales="Object.values(locales)" />
    </template>
    

You can use it with Vue i18n:

    
    
    <script setup lang="ts">
    import { useI18n } from 'vue-i18n'
    import * as locales from '@nuxt/ui/locale'
    
    const { locale } = useI18n()
    </script>
    
    <template>
      <ULocaleSelect v-model="locale" :locales="Object.values(locales)" />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`trailingIcon`| `appConfig.ui.icons.chevronDown`| ` string`The icon displayed
to open the menu.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with listbox  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`modelValue`| | ` string`  
`content`| `{ side: 'bottom', sideOffset: 8, collisionPadding: 8, position:
'popper' }`| ` ComboboxContentProps &
Partial<EmitsToProps<DismissableLayerEmits>>`The content of the menu.Show
properties

  * `position?: "inline" | "popper"`The positioning mode to use,   
`inline` is the default and you can control the position using CSS.  
`popper` positions content in the same way as our other primitives, for
example `Popover` or `DropdownMenu`.

  * `bodyLock?: boolean`The document.body will be lock, and scrolling will be disabled.
  * `side?: "top" | "bottom" | "right" | "left"`The preferred side of the trigger to render against when open. Will be reversed when collisions occur and avoidCollisions is enabled. Defaults to `"top"`.
  * `sideOffset?: number`The distance in pixels from the trigger. Defaults to `0`.
  * `align?: "end" | "start" | "center"`The preferred alignment against the trigger. May change when collisions occur. Defaults to `"center"`.
  * `alignOffset?: number`An offset in pixels from the `start` or `end` alignment options. Defaults to `0`.
  * `avoidCollisions?: boolean`When `true`, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to `true`.
  * `collisionBoundary?: Element | (Element | null)[] | null`The element used as the collision boundary. By default this is the viewport, though you can provide additional element(s) to be included in this check. Defaults to `[]`.
  * `collisionPadding?: number | Partial<Record<"top" | "bottom" | "right" | "left", number>>`The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { top: 20, left: 20 }. Defaults to `0`.
  * `arrowPadding?: number`The padding between the arrow and the edges of the content. If your content has border-radius, this will prevent it from overflowing the corners. Defaults to `0`.
  * `sticky?: "partial" | "always"`The sticky behavior on the align axis. `partial` will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to `"partial"`.
  * `hideWhenDetached?: boolean`Whether to hide the content when the trigger becomes fully occluded. Defaults to `false`.
  * `positionStrategy?: "fixed" | "absolute"`The type of CSS position property to use.
  * `updatePositionStrategy?: "always" | "optimized"`Strategy to update the position of the floating element on every animation frame. Defaults to `'optimized'`.
  * `disableUpdateOnLayoutShift?: boolean`Whether to disable the update position for the content when the layout shifted. Defaults to `false`.
  * `prioritizePosition?: boolean`Force content to be position within the viewport.Might overlap the reference element, which may not be desired. Defaults to `false`.
  * `reference?: ReferenceElement`The custom element or virtual element that will be set as the reference to position the floating element.If provided, it will replace the default anchor element.
  * `disableOutsidePointerEvents?: boolean`When `true`, hover/focus/click interactions will be disabled on elements outside the `DismissableLayer`. Users will need to click twice on outside elements to interact with them: once to close the `DismissableLayer`, and again to trigger the element.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`

  
`variant`| `'outline'`| ` "outline" | "soft" | "subtle" | "ghost" | "none"`  
`selectedIcon`| `appConfig.ui.icons.check`| ` string`The icon displayed when
an item is selected.  
`arrow`| `false`| `boolean | ComboboxArrowProps`Display an arrow alongside the menu.  
`portal`| `true`| ` string | false | true | HTMLElement`Render the menu in a portal.  
`locales`| | ` Locale<any>[]`Show properties

  * `name: string`
  * `code: string`
  * `dir: Direction`
  * `messages: any`

  
`ui`| | ` { base?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; ... 21 more ...; focusScope?: ClassNameValue; }`  
  
[LinkA wrapper around <NuxtLink> with extra props.](/components/link)[MainA
main element that fills the available viewport height.](/components/main)

