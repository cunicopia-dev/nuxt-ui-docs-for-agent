<!-- source: https://ui.nuxt.com/components/carousel --> # Carousel

[Embla](https://www.embla-
carousel.com/api/)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Carousel.vue)

A carousel with motion and swipe built using Embla.

## Usage

### Items

Use the `items` prop as an array and render each item using the default slot:

Use your mouse to drag the carousel horizontally on desktop.

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    </script>
    
    <template>
      <UCarousel v-slot="{ item }" :items="items" class="w-full max-w-xs mx-auto">
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

You can control how many items are visible by using the
[`basis`](https://tailwindcss.com/docs/flex-basis) /
[`width`](https://tailwindcss.com/docs/width) utility classes on the `item`:

![](https://picsum.photos/468/468?random=1)

![](https://picsum.photos/468/468?random=2)

![](https://picsum.photos/468/468?random=3)

![](https://picsum.photos/468/468?random=4)

![](https://picsum.photos/468/468?random=5)

![](https://picsum.photos/468/468?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/468/468?random=1',
      'https://picsum.photos/468/468?random=2',
      'https://picsum.photos/468/468?random=3',
      'https://picsum.photos/468/468?random=4',
      'https://picsum.photos/468/468?random=5',
      'https://picsum.photos/468/468?random=6'
    ]
    </script>
    
    <template>
      <UCarousel v-slot="{ item }" :items="items" :ui="{ item: 'basis-1/3' }">
        <img :src="item" width="234" height="234" class="rounded-lg">
      </UCarousel>
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the Progress. Defaults
to `horizontal`.

Use your mouse to drag the carousel vertically on desktop.

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        orientation="vertical"
        :items="items"
        class="w-full max-w-xs mx-auto"
        :ui="{ container: 'h-[336px]' }"
      >
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

You need to specify a `height` on the container in vertical orientation.

### Arrows

Use the `arrows` prop to display prev and next buttons.

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    </script>
    
    <template>
      <UCarousel v-slot="{ item }" arrows :items="items" class="w-full max-w-xs mx-auto">
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

### Prev / Next

Use the `prev` and `next` props to customize the prev and next buttons with
any [Button](/components/button) props.

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        arrows
        :prev="{ color: 'primary' }"
        :next="{ variant: 'solid' }"
        :items="items"
        class="w-full max-w-xs mx-auto"
      >
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

### Prev / Next Icons

Use the `prev-icon` and `next-icon` props to customize the buttons
[Icon](/components/icon). Defaults to `i-lucide-arrow-left` / `i-lucide-arrow-
right`.

prevIcon

nextIcon

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    defineProps<{
      prevIcon?: string
      nextIcon?: string
    }>()
    
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        arrows
        :prev-icon="prevIcon"
        :next-icon="nextIcon"
        :items="items"
        class="w-full max-w-xs mx-auto"
      >
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize these icons globally in
your `app.config.ts` under `ui.icons.arrowLeft` / `ui.icons.arrowRight` key.

[](/getting-started/icons/vue#theme)You can customize these icons globally in
your `vite.config.ts` under `ui.icons.arrowLeft` / `ui.icons.arrowRight` key.

### Dots

Use the `dots` prop to display a list of dots to scroll to a specific slide.

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    </script>
    
    <template>
      <UCarousel v-slot="{ item }" dots :items="items" class="w-full max-w-xs mx-auto">
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

The number of dots is based on the number of slides displayed in the view:

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    </script>
    
    <template>
      <UCarousel v-slot="{ item }" dots :items="items" :ui="{ item: 'basis-1/3' }">
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

## Plugins

The Carousel component implements the official [Embla Carousel
plugins](https://www.embla-carousel.com/plugins/).

### Autoplay

This plugin is used to extend Embla Carousel with **autoplay** functionality.

Use the `autoplay` prop as a boolean or an object to configure the [Autoplay
plugin](https://www.embla-carousel.com/plugins/autoplay/).

![](https://picsum.photos/468/468?random=1)

![](https://picsum.photos/468/468?random=2)

![](https://picsum.photos/468/468?random=3)

![](https://picsum.photos/468/468?random=4)

![](https://picsum.photos/468/468?random=5)

![](https://picsum.photos/468/468?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/468/468?random=1',
      'https://picsum.photos/468/468?random=2',
      'https://picsum.photos/468/468?random=3',
      'https://picsum.photos/468/468?random=4',
      'https://picsum.photos/468/468?random=5',
      'https://picsum.photos/468/468?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        loop
        arrows
        dots
        :autoplay="{ delay: 2000 }"
        :items="items"
        :ui="{ item: 'basis-1/3' }"
      >
        <img :src="item" width="234" height="234" class="rounded-lg">
      </UCarousel>
    </template>
    

In this example, we're using the `loop` prop for an infinite carousel.

### Auto Scroll

This plugin is used to extend Embla Carousel with **auto scroll**
functionality.

Use the `auto-scroll` prop as a boolean or an object to configure the [Auto
Scroll plugin](https://www.embla-carousel.com/plugins/auto-scroll/).

![](https://picsum.photos/468/468?random=1)

![](https://picsum.photos/468/468?random=2)

![](https://picsum.photos/468/468?random=3)

![](https://picsum.photos/468/468?random=4)

![](https://picsum.photos/468/468?random=5)

![](https://picsum.photos/468/468?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/468/468?random=1',
      'https://picsum.photos/468/468?random=2',
      'https://picsum.photos/468/468?random=3',
      'https://picsum.photos/468/468?random=4',
      'https://picsum.photos/468/468?random=5',
      'https://picsum.photos/468/468?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        loop
        dots
        arrows
        auto-scroll
        :items="items"
        :ui="{ item: 'basis-1/3' }"
      >
        <img :src="item" width="234" height="234" class="rounded-lg">
      </UCarousel>
    </template>
    

In this example, we're using the `loop` prop for an infinite carousel.

### Auto Height

This plugin is used to extend Embla Carousel with **auto height**
functionality. It changes the height of the carousel container to fit the
height of the highest slide in view.

Use the `auto-height` prop as a boolean or an object to configure the [Auto
Height plugin](https://www.embla-carousel.com/plugins/auto-height/).

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/320?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/320?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/320?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/320?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/320?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/320?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        auto-height
        arrows
        dots
        :items="items"
        :ui="{
          container: 'transition-[height]',
          controls: 'absolute -top-8 inset-x-12',
          dots: '-top-7',
          dot: 'w-6 h-1'
        }"
        class="w-full max-w-xs mx-auto"
      >
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

In this example, we add the `transition-[height]` class on the container to
animate the height change.

### Class Names

Class Names is a **class name toggle** utility plugin for Embla Carousel that
enables you to automate the toggling of class names on your carousel.

Use the `class-names` prop as a boolean or an object to configure the [Class
Names plugin](https://www.embla-carousel.com/plugins/class-names/).

![](https://picsum.photos/528/528?random=1)

![](https://picsum.photos/528/528?random=2)

![](https://picsum.photos/528/528?random=3)

![](https://picsum.photos/528/528?random=4)

![](https://picsum.photos/528/528?random=5)

![](https://picsum.photos/528/528?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/528/528?random=1',
      'https://picsum.photos/528/528?random=2',
      'https://picsum.photos/528/528?random=3',
      'https://picsum.photos/528/528?random=4',
      'https://picsum.photos/528/528?random=5',
      'https://picsum.photos/528/528?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        class-names
        arrows
        :items="items"
        :ui="{
          item: 'basis-[70%] transition-opacity [&:not(.is-snapped)]:opacity-10'
        }"
        class="mx-auto max-w-sm"
      >
        <img :src="item" width="264" height="264" class="rounded-lg">
      </UCarousel>
    </template>
    

In this example, we add the `transition-opacity [&:not(.is-
snapped)]:opacity-10` classes on the `item` to animate the opacity change.

### Fade

This plugin is used to replace the Embla Carousel scroll functionality with
**fade transitions**.

Use the `fade` prop as a boolean or an object to configure the [Fade
plugin](https://www.embla-carousel.com/plugins/fade/).

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        fade
        arrows
        dots
        :items="items"
        class="w-full max-w-xs mx-auto"
      >
        <img :src="item" width="320" height="320" class="rounded-lg">
      </UCarousel>
    </template>
    

### Wheel Gestures

This plugin is used to extend Embla Carousel with the ability to **use the
mouse/trackpad wheel** to navigate the carousel.

Use the `wheel-gestures` prop as a boolean or an object to configure the
[Wheel Gestures plugin](https://www.embla-carousel.com/plugins/wheel-
gestures/).

Use your mouse wheel to scroll the carousel.

![](https://picsum.photos/468/468?random=1)

![](https://picsum.photos/468/468?random=2)

![](https://picsum.photos/468/468?random=3)

![](https://picsum.photos/468/468?random=4)

![](https://picsum.photos/468/468?random=5)

![](https://picsum.photos/468/468?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/468/468?random=1',
      'https://picsum.photos/468/468?random=2',
      'https://picsum.photos/468/468?random=3',
      'https://picsum.photos/468/468?random=4',
      'https://picsum.photos/468/468?random=5',
      'https://picsum.photos/468/468?random=6'
    ]
    </script>
    
    <template>
      <UCarousel
        v-slot="{ item }"
        loop
        wheel-gestures
        :items="items"
        :ui="{ item: 'basis-1/3' }"
      >
        <img :src="item" width="234" height="234" class="rounded-lg">
      </UCarousel>
    </template>
    

## Examples

### With thumbnails

You can use the `emblaApi` function [scrollTo](https://www.embla-
carousel.com/api/methods/#scrollto) to display thumbnails under the carousel
that allows you to navigate to a specific slide.

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

![](https://picsum.photos/640/640?random=1)

![](https://picsum.photos/640/640?random=2)

![](https://picsum.photos/640/640?random=3)

![](https://picsum.photos/640/640?random=4)

![](https://picsum.photos/640/640?random=5)

![](https://picsum.photos/640/640?random=6)

    
    
    <script setup lang="ts">
    const items = [
      'https://picsum.photos/640/640?random=1',
      'https://picsum.photos/640/640?random=2',
      'https://picsum.photos/640/640?random=3',
      'https://picsum.photos/640/640?random=4',
      'https://picsum.photos/640/640?random=5',
      'https://picsum.photos/640/640?random=6'
    ]
    
    const carousel = useTemplateRef('carousel')
    const activeIndex = ref(0)
    
    function onClickPrev() {
      activeIndex.value--
    }
    function onClickNext() {
      activeIndex.value++
    }
    
    function onSelect(index: number) {
      activeIndex.value = index
    
      carousel.value?.emblaApi?.scrollTo(index)
    }
    </script>
    
    <template>
      <div class="flex-1 w-full">
        <UCarousel
          ref="carousel"
          v-slot="{ item }"
          arrows
          :items="items"
          :prev="{ onClick: onClickPrev }"
          :next="{ onClick: onClickNext }"
          class="w-full max-w-xs mx-auto"
        >
          <img :src="item" width="320" height="320" class="rounded-lg">
        </UCarousel>
    
        <div class="flex gap-1 justify-between pt-4 max-w-xs mx-auto">
          <div
            v-for="(item, index) in items"
            :key="index"
            class="size-11 opacity-25 hover:opacity-100 transition-opacity"
            :class="{ 'opacity-100': activeIndex === index }"
            @click="onSelect(index)"
          >
            <img :src="item" width="44" height="44" class="rounded-lg">
          </div>
        </div>
      </div>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`prev`| `{ size: 'md', color: 'neutral', variant: 'link' }`| `
ButtonProps`Configure the prev button when arrows are enabled.Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "xs" | "sm" | "md" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`prevIcon`| `appConfig.ui.icons.arrowLeft`| ` string`The icon displayed in the
prev button.  
`next`| `{ size: 'md', color: 'neutral', variant: 'link' }`| `
ButtonProps`Configure the next button when arrows are enabled.Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "xs" | "sm" | "md" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`nextIcon`| `appConfig.ui.icons.arrowRight`| ` string`The icon displayed in
the next button.  
`arrows`| `false`| `boolean`Display prev and next buttons to scroll the
carousel.  
`dots`| `false`| `boolean`Display dots to scroll to a specific slide.  
`orientation`| `'horizontal'`| ` "vertical" | "horizontal"`The orientation of the carousel.  
`items`| | ` AcceptableValue[]`  
`autoplay`| `false`| `boolean | Partial<CreateOptionsType<OptionsType>>`Enable Autoplay plugin

  * <https://www.embla-carousel.com/plugins/autoplay/>

  
`autoScroll`| `false`| `boolean | Partial<CreateOptionsType<OptionsType>>`Enable Auto Scroll plugin

  * <https://www.embla-carousel.com/plugins/auto-scroll/>

  
`autoHeight`| `false`| `boolean | Partial<CreateOptionsType<{ active: boolean; breakpoints: { [key: string]: Omit<Partial<...>, "breakpoints">; }; }>>`Enable Auto Height plugin

  * <https://www.embla-carousel.com/plugins/auto-height/>

  
`classNames`| `false`| `boolean | Partial<CreateOptionsType<OptionsType>>`Enable Class Names plugin

  * <https://www.embla-carousel.com/plugins/class-names/>

  
`fade`| `false`| `boolean | Partial<CreateOptionsType<{ active: boolean; breakpoints: { [key: string]: Omit<Partial<...>, "breakpoints">; }; }>>`Enable Fade plugin

  * <https://www.embla-carousel.com/plugins/fade/>

  
`wheelGestures`| `false`| `any`Enable Wheel Gestures plugin

  * <https://www.embla-carousel.com/plugins/wheel-gestures/>

  
`align`| `'center'`| ` "start" | "center" | "end" | (viewSize: number, snapSize: number, index: number): number`  
`containScroll`| `'trimSnaps'`| ` false | "trimSnaps" | "keepSnaps"`  
`slidesToScroll`| `1`| ` number | "auto"`  
`dragFree`| `false`| `boolean`  
`dragThreshold`| `10`| ` number`  
`inViewThreshold`| `0`| ` number | number[]`  
`loop`| `false`| `boolean`  
`skipSnaps`| `false`| `boolean`  
`duration`| `25`| ` number`  
`startIndex`| `0`| ` number`  
`watchDrag`| `true`| ` false | true | (emblaApi: EmblaCarouselType, evt: PointerEventType): boolean | void`  
`watchResize`| `true`| ` false | true | (emblaApi: EmblaCarouselType, entries: ResizeObserverEntry[]): boolean | void`  
`watchSlides`| `true`| ` false | true | (emblaApi: EmblaCarouselType, mutations: MutationRecord[]): boolean | void`  
`watchFocus`| `true`| ` false | true | (emblaApi: EmblaCarouselType, evt: FocusEvent): boolean | void`  
`active`| `true`| `boolean`  
`breakpoints`| `{}`| ` { [key: string]: Omit<Partial<CreateOptionsType<{ align: AlignmentOptionType; axis: AxisOptionType; container: string | HTMLElement | null; slides: string | HTMLElement[] | NodeListOf<...> | null; ... 13 more ...; watchFocus: FocusHandlerOptionType; }>>, "breakpoints">; }`  
`ui`| | ` { root?: ClassNameValue; viewport?: ClassNameValue; container?: ClassNameValue; item?: ClassNameValue; controls?: ClassNameValue; ... 4 more ...; dot?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ item: AcceptableValue; index: number; }`  
  
### Emits

Event |  Type   
---|---  
`select`| `[selectedIndex: number]`  
  
### Expose

You can access the typed component instance using
[`useTemplateRef`](https://vuejs.org/api/composition-api-
helpers.html#usetemplateref).

    
    
    <script setup lang="ts">
    const carousel = useTemplateRef('carousel')
    </script>
    
    <template>
      <UCarousel ref="carousel" />
    </template>
    

This will give you access to the following:

Name| Type  
---|---  
`emblaRef`| `Ref<HTMLElement | null>`  
`emblaApi`| [`Ref<EmblaCarouselType | null>`](https://www.embla-carousel.com/api/methods/#typescript)  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        carousel: {
          slots: {
            root: 'relative focus:outline-none',
            viewport: 'overflow-hidden',
            container: 'flex items-start',
            item: 'min-w-0 shrink-0 basis-full',
            controls: '',
            arrows: '',
            prev: 'absolute rounded-full',
            next: 'absolute rounded-full',
            dots: 'absolute inset-x-0 -bottom-7 flex flex-wrap items-center justify-center gap-3',
            dot: [
              'cursor-pointer size-3 bg-accented rounded-full',
              'transition'
            ]
          },
          variants: {
            orientation: {
              vertical: {
                container: 'flex-col -mt-4',
                item: 'pt-4',
                prev: 'top-4 sm:-top-12 left-1/2 -translate-x-1/2 rotate-90 rtl:-rotate-90',
                next: 'bottom-4 sm:-bottom-12 left-1/2 -translate-x-1/2 rotate-90 rtl:-rotate-90'
              },
              horizontal: {
                container: 'flex-row -ms-4',
                item: 'ps-4',
                prev: 'start-4 sm:-start-12 top-1/2 -translate-y-1/2',
                next: 'end-4 sm:-end-12 top-1/2 -translate-y-1/2'
              }
            },
            active: {
              true: {
                dot: 'bg-inverted'
              }
            }
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            carousel: {
              slots: {
                root: 'relative focus:outline-none',
                viewport: 'overflow-hidden',
                container: 'flex items-start',
                item: 'min-w-0 shrink-0 basis-full',
                controls: '',
                arrows: '',
                prev: 'absolute rounded-full',
                next: 'absolute rounded-full',
                dots: 'absolute inset-x-0 -bottom-7 flex flex-wrap items-center justify-center gap-3',
                dot: [
                  'cursor-pointer size-3 bg-accented rounded-full',
                  'transition'
                ]
              },
              variants: {
                orientation: {
                  vertical: {
                    container: 'flex-col -mt-4',
                    item: 'pt-4',
                    prev: 'top-4 sm:-top-12 left-1/2 -translate-x-1/2 rotate-90 rtl:-rotate-90',
                    next: 'bottom-4 sm:-bottom-12 left-1/2 -translate-x-1/2 rotate-90 rtl:-rotate-90'
                  },
                  horizontal: {
                    container: 'flex-row -ms-4',
                    item: 'ps-4',
                    prev: 'start-4 sm:-start-12 top-1/2 -translate-y-1/2',
                    next: 'end-4 sm:-end-12 top-1/2 -translate-y-1/2'
                  }
                },
                active: {
                  true: {
                    dot: 'bg-inverted'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            carousel: {
              slots: {
                root: 'relative focus:outline-none',
                viewport: 'overflow-hidden',
                container: 'flex items-start',
                item: 'min-w-0 shrink-0 basis-full',
                controls: '',
                arrows: '',
                prev: 'absolute rounded-full',
                next: 'absolute rounded-full',
                dots: 'absolute inset-x-0 -bottom-7 flex flex-wrap items-center justify-center gap-3',
                dot: [
                  'cursor-pointer size-3 bg-accented rounded-full',
                  'transition'
                ]
              },
              variants: {
                orientation: {
                  vertical: {
                    container: 'flex-col -mt-4',
                    item: 'pt-4',
                    prev: 'top-4 sm:-top-12 left-1/2 -translate-x-1/2 rotate-90 rtl:-rotate-90',
                    next: 'bottom-4 sm:-bottom-12 left-1/2 -translate-x-1/2 rotate-90 rtl:-rotate-90'
                  },
                  horizontal: {
                    container: 'flex-row -ms-4',
                    item: 'ps-4',
                    prev: 'start-4 sm:-start-12 top-1/2 -translate-y-1/2',
                    next: 'end-4 sm:-end-12 top-1/2 -translate-y-1/2'
                  }
                },
                active: {
                  true: {
                    dot: 'bg-inverted'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[CardDisplay content in a card with a header, body and
footer.](/components/card)[CheckboxAn input element to toggle between checked
and unchecked states.](/components/checkbox)

